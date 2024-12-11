from datetime import datetime
from Clients_Functions import Clients

c = Clients

class Clients_Manager:
    def __init__(self, st="trails.csv", tf = "clients.csv") -> None:
        self.Visits = tf
        self.trails = st

    def saveVisits(self, tr):
        file = open(self.Visits, "a", encoding="utf-8")
        file.write(tr + "\n")

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

    def Create_Client(self):
        age_list = {"1":"12-18","2":"19-29","3":"30-49","4":"50-64","5":"65+"}
        sat_list = {"1":"Very Unsatisfied","2":"Unsatisfied","3":"Undecided","4":"Satisfied","5":"Very Satisfied"}
        while True:
            name = input('Client name -> ').strip()
            if not name:
                print('Name cannot be empty. Please enter a valid Client name.')
                continue
            break

        while True:
            country = input('Country name -> ').strip()
            if not country:
                print('Country cannot be empty. Please enter a valid Country name.')
                continue
            break

        while True:
            gender = input('Gender -> ').strip()
            if not gender:
                print('Gender cannot be empty. Please enter a valid Gender.')
                continue
            break

        while True:
            print("1. 12-18, 2. 19-29, 3.  30-49, 4. 50-64, 5. +65")
            choice = input("Insert the number corresponding to your Age Group -> ")
            if choice not in age_list:
                print("Invalid number. Please try again.")
                continue
            age_group = age_list[choice]
            break

        while True:
            print("1. (very dissatisfied), 2 (dissatisfied), 3 (indifferent), 4 (satisfied) and 5 (very satisfied5")
            choice = input("Insert the number corresponding to your satisfaction -> ")
            if choice not in sat_list:
                print("Invalid number. Please try again.")
                continue
            satis = sat_list[choice]
            break

        while True:
            date = input("Date (d/m/y): ")  # Prompt for date
            try:
                date = datetime.strptime(date, "%m/%d/%Y").date()  # Include time in format
                break
            except ValueError:
                print("Invalid check IN format. Please use 'd/m/y'.")

        Visits = c.Visits(name,country,gender,age_group,satis,date,self.trails)
        self.saveVisits(Visits.format())
        print(f"Client {name} Added.")