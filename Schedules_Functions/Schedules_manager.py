from Schedules_Functions import Schedules  # Import the Schedules class from the Schedules_Functions module
from datetime import datetime
import json

a = Schedules  # Create an instance of the Schedules class

class SchedulesManager:
    def __init__(self, schedule = "schedule.csv", trails = "trails.csv", guide = "guide.json"):
        #Initialize the SchedulesManager with file names and optional found guide/trail.
        self.schedule = schedule  # Set the filename for schedules
        self.trails = trails  # Set the filename for trails
        self.guide = guide  # Set the filename for guides
        self.guide_found = ""
        self.trail_found = ""

    def save_schedules(self, schedule_entry):
        #Append a new schedule entry to the schedules file.
        with open(self.schedule, 'a', encoding='utf-8') as file:
            file.write(schedule_entry + "\n")  # Write the schedule entry followed by a newline for proper CSV formatting

    def find_Trail(self):
        while True:
            trail_ID_input = input("Enter trail ID: ").strip()  # Prompt user for trail ID
            if not trail_ID_input:
                print("Trail ID cannot be empty. Please try again.")  # Ensure input is not empty
                continue
            try:
                trail_ID = int(trail_ID_input)  # Convert input to an integer
            except ValueError:
                print("Invalid trail ID. Please enter a number.")  # Handle non-integer input
                continue

            with open(self.trails, 'r', encoding='utf-8') as file:  # Open trails file for reading
                for line in file:
                    trail_data = line.strip().split(";")  # Split line into components using ';' as delimiter
                    if str(trail_ID) == trail_data[0]:  # Check if the first element matches the trail ID
                        self.trail_found = trail_data[1]  # Store the found trail name
                        print(f"Trail found: {self.trail_found}")  # Inform user of found trail
                        return  # Exit the method if a trail is found

            print(f"No trail found with ID: {trail_ID}")  # Inform user that no matching trail was found

    def findGuide(self):
        while True:
            guide_ID_input = input("Enter guide ID: ").strip()  # Prompt user for guide ID
            if not guide_ID_input:
                print("Guide ID cannot be empty. Please try again.")  # Ensure input is not empty
                continue

            with open(self.guide, 'r', encoding='utf-8') as file:  # Open guides file for reading
                data = json.load(file)  # Load existing guides from JSON file

            for guide in data:
                if guide["id"] == guide_ID_input:  # Compare as strings to find matching guide ID
                    self.guide_found = guide["name"]  # Store the found guide name
                    print(f"Guide found: {self.guide_found}")  # Inform user of found guide
                    return  # Exit the method if a guide is found

            print(f"No guide found with ID: {guide_ID_input}")  # Inform user that no matching guide was found

    def CheckIn_and_Out(self):
        while True:
            self.find_Trail()  # Find and set the selected trail using find_Trail method
            if self.trail_found:  # If a trail was found, break the loop
                break  # Exit loop if a valid trail is selected

        while True:
            self.findGuide()  # Find and set the selected guide using findGuide method
            if self.guide_found:  # If a guide was found, break the loop
                break  # Exit loop if a valid guide is selected

        while True:
            try:
                check_IN = input("Check IN (d/m/y H:M): ")
                check_IN = datetime.strptime(check_IN, "%d/%m/%Y %H:%M")  # Convert input string to datetime object
                break
            except ValueError:
                print("Invalid check IN format. Please use 'd/m/y H:M'.")

        while True:
            try:
                check_OUT = input("Check OUT (d/m/y H:M): ")
                check_OUT = datetime.strptime(check_OUT, "%d/%m/%Y %H:%M")
                break
            except ValueError:
                print("Invalid check OUT format. Please use 'd/m/y H:M'.")

        # Create a new schedule entry using stored values for selected trail and guide
        schedule_entry = a.Schedules(self.guide_found, self.trail_found, check_IN, check_OUT)
        self.save_schedules(
            schedule_entry.format())  # Save the formatted schedule entry to the CSV file using save_schedules method
        print("Schedule added.")  # Confirm successful addition of the schedule entry
