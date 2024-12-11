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
            guide_ID_input = input("Enter guide ID: ").strip()
            if not guide_ID_input:
                print("Guide ID cannot be empty. Please try again.")
                continue
            try:
                guide_ID = int(guide_ID_input)
                break
            except ValueError:
                print("Invalid guide ID. Please enter a number.")

        guide_found = False
        with open(self.guide, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for guide in data:
            if guide["id"] == guide_ID:
                self.found_Guide = guide["name"]
                guide_found = True
                break  # Saia do loop assim que encontrar o guia

        if guide_found:
            print(f"Guide found: {self.found_Guide}")
        else:
            print(f"No guide found with ID: {guide_ID}")

    def CheckIn_and_Out(self):
        self.find_Trail()
        self.findGuide()

        while True:
            try:
                check_IN = input("Check IN: (d/m/y): ")
                check_IN = datetime.strptime(check_IN, "%m/%d/%Y")
                break
            except ValueError:
                print("Invalid check IN")
        while True:
            try:
                check_OUT = input("Check OUT: (d/m/y): ")
                check_OUT = datetime.strptime(check_OUT, "%m/%d/%Y")
                break
            except ValueError:
                print("Invalid check IN")
        schedule = a.Schedules(self.found_Trail,self.found_Guide,check_IN,check_OUT)
        self.save_schedules(schedule.format())
        print("Schedule added.")
