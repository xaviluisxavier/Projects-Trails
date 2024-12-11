from Schedules_Functions import Schedules
from datetime import datetime
import json

a = Schedules
class SchedulesManager:
    def __init__(self, guide_found = "",trail_found = "",
                 schedule = "schedule.csv",trails = "trails.csv", guide = "guide.json"):
        self.schedule = schedule
        self.trails = trails
        self.guide = guide
        self.guide_found = guide_found
        self.trail_found = trail_found

    def save_schedules(self, tf):
        file = open(self.schedule, 'a', encoding='utf-8')
        file.write(tf)

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
                if str(trail_ID) == trail_data[0]:
                    self.found_Trail = trail_data[1]
                    trail_found = True
                    break
        if trail_found:
            print(f"Trail found: {self.found_Trail}")
        else:
            print(f"No trail found with ID: {trail_ID}")

    def findGuide(self):
        while True:
            # Prompt user for guide ID
            guide_ID_input = input("Enter guide ID: ").strip()
            if not guide_ID_input:
                print("Guide ID cannot be empty. Please try again.")
                continue

            # Keep the guide ID as a string
            guide_ID = guide_ID_input
            break

        guide_found = False
        # Open the JSON file and load data
        with open(self.guide, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Search for the guide by ID
        for guide in data:
            if guide["id"] == guide_ID:  # Compare as strings
                self.found_Guide = guide["name"]
                guide_found = True
                break  # Exit loop upon finding the guide

        # Output result
        if guide_found:
            print(f"Guide found: {self.found_Guide}")
        else:
            print(f"No guide found with ID: {guide_ID}")

    def CheckIn_and_Out(self):
        self.find_Trail()
        self.findGuide()

        while True:
            try:
                check_IN = input("Check IN (d/m/y H:M): ")  # Prompt for date and time
                check_IN = datetime.strptime(check_IN, "%m/%d/%Y %H:%M")  # Include time in format
                break
            except ValueError:
                print("Invalid check IN format. Please use 'd/m/y H:M'.")

        while True:
            try:
                check_OUT = input("Check OUT (d/m/y H:M): ")  # Prompt for date and time
                check_OUT = datetime.strptime(check_OUT, "%m/%d/%Y %H:%M")  # Include time in format
                break
            except ValueError:
                print("Invalid check OUT format. Please use 'd/m/y H:M'.")

        schedule = a.Schedules(self.find_Trail(), self.findGuide(), check_IN, check_OUT)
        self.save_schedules(schedule.format())
        print("Schedule added.")

