from Schedules_Functions import Schedules
from datetime import datetime
import json

a = Schedules
from Schedules_Functions import Schedules
from datetime import datetime
import json


class SchedulesManager:
    def __init__(self, guide_found="", trail_found="", schedule="schedule.csv", trails="trails.csv",
                 guide="guide.json"):
        self.schedule = schedule
        self.trails = trails
        self.guide = guide
        self.guide_found = guide_found
        self.trail_found = trail_found

    def save_schedules(self, tf):
        with open(self.schedule, 'a', encoding='utf-8') as file:
            file.write(tf + "\n")  # Add newline for proper CSV formatting

    def find_Trail(self):
        while True:
            trail_ID_input = input("Enter trail ID: ").strip()
            if not trail_ID_input:
                print("Trail ID cannot be empty. Please try again.")
                continue
            try:
                trail_ID = int(trail_ID_input)
                break
            except ValueError:
                print("Invalid trail ID. Please enter a number.")

        trail_found = False
        with open(self.trails, 'r', encoding='utf-8') as file:
            for line in file:
                trail_data = line.strip().split(";")
                if str(trail_ID) == trail_data[0]:  # Assuming the first column is the ID
                    self.trail_found = trail_data[1]  # Store the found trail name
                    trail_found = True
                    break

        if trail_found:
            print(f"Trail found: {self.trail_found}")
        else:
            print(f"No trail found with ID: {trail_ID}")

    def findGuide(self):
        while True:
            guide_ID_input = input("Enter guide ID: ").strip()
            if not guide_ID_input:
                print("Guide ID cannot be empty. Please try again.")
                continue
            guide_ID = guide_ID_input  # Keep the guide ID as a string
            break
        guide_found = False
        with open(self.guide, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for guide in data:
            if guide["id"] == guide_ID:  # Compare as strings
                self.guide_found = guide["name"]  # Store the found guide name
                guide_found = True
                break

        if guide_found:
            print(f"Guide found: {self.guide_found}")
        else:
            print(f"No guide found with ID: {guide_ID}")

    def CheckIn_and_Out(self):
        self.find_Trail()  # This will set self.trail_found
        self.findGuide()  # This will set self.guide_found

        while True:
            try:
                check_IN = input("Check IN (d/m/y H:M): ")
                check_IN = datetime.strptime(check_IN, "%m/%d/%Y %H:%M")
                break
            except ValueError:
                print("Invalid check IN format. Please use 'd/m/y H:M'.")

        while True:
            try:
                check_OUT = input("Check OUT (d/m/y H:M): ")
                check_OUT = datetime.strptime(check_OUT, "%m/%d/%Y %H:%M")
                break
            except ValueError:
                print("Invalid check OUT format. Please use 'd/m/y H:M'.")
        # Create the schedule using stored values for trail and guide
        schedule_entry = a.Schedules(self.guide_found, self.trail_found, check_IN, check_OUT)
        # Save the formatted schedule entry to the CSV file
        self.save_schedules(schedule_entry.format())

        print("Schedule added.")

