from datetime import datetime
from Clients_Functions import Clients  # Import the Clients class from Clients_Functions module

c = Clients  # Create an instance of the Clients class (though this line is not used correctly)

class Clients_Manager:
    def __init__(self, ts="trails.csv", vs="clients.csv") -> None:
        #Initialize the Clients_Manager with default trail and client file names.
        self.Visits = vs  # Set the filename for client visits
        self.trails = ts  # Set the filename for trails

    def saveVisits(self, visit):
        #Append a new visit record to the Visits file.
        with open(self.Visits, "a", encoding="utf-8") as file:  # Open and close the Visits file in append mode
            file.write(visit + "\n")  # Write the visit record followed by a newline


    def find_Trail(self):
        #Find a trail by its ID.
        while True:
            trail_ID_input = input("Enter trail ID: ").strip()  # Prompt user for trail ID
            if not trail_ID_input:
                print("Trail ID cannot be empty. Please try again.")  # Ensure input is not empty
                continue
            try:
                trail_ID = int(trail_ID_input)  # Convert input to an integer
                break  # Exit loop if conversion is successful
            except ValueError:
                print("Invalid trail ID. Please enter a number.")  # Handle non-integer input

        trail_found = False  # Flag to check if the trail was found
        with open(self.trails, 'r', encoding='utf-8') as file:  # Open trails file for reading
            for line in file:
                trail_data = line.strip().split(";")  # Split line into components using ';' as delimiter
                if str(trail_ID) == trail_data[0]:  # Check if the first element matches the trail ID
                    self.found_Trail = trail_data[1]  # Store the found trail name
                    trail_found = True  # Set flag to indicate a trail was found
                    break  # Exit loop if trail is found
        if trail_found:
            print(f"Trail found: {self.found_Trail}")  # Inform user of found trail
        else:
            print(f"No trail found with ID: {trail_ID}")  # Inform user that no matching trail was found

    def Create_Client(self):
        #Create a new client record.
        age_list = {"1": "12-18", "2": "19-29", "3": "30-49", "4": "50-64", "5": "65+"}  # Age groups mapping
        sat_list = {"1": "Very Unsatisfied", "2": "Unsatisfied", "3": "Undecided", "4": "Satisfied",
                    "5": "Very Satisfied"}  # Satisfaction levels mapping

        while True:
            name = input('Client name -> ').strip()  # Prompt for client name
            if not name:
                print('Name cannot be empty. Please enter a valid Client name.')  # Validate input
                continue
            break

        while True:
            country = input('Country name -> ').strip()  # Prompt for country name
            if not country:
                print('Country cannot be empty. Please enter a valid Country name.')  # Validate input
                continue
            break

        while True:
            gender = input('Gender -> ').strip()  # Prompt for gender
            if not gender:
                print('Gender cannot be empty. Please enter a valid Gender.')  # Validate input
                continue
            break

        while True:
            print("1. 12-18, 2. 19-29, 3. 30-49, 4. 50-64, 5. +65")  # Display age group options
            choice = input("Insert the number corresponding to your Age Group -> ")  # Prompt for age group choice
            if choice not in age_list:
                print("Invalid number. Please try again.")  # Validate input choice
                continue
            age_group = age_list[choice]  # Get corresponding age group from dictionary
            break

        while True:
            print("1. (very dissatisfied), 2 (dissatisfied), 3 (indifferent), 4 (satisfied), and 5 (very satisfied)")
            choice = input("Insert the number corresponding to your satisfaction -> ")
            if choice not in sat_list:
                print("Invalid number. Please try again.")
                continue
            satis = sat_list[choice]
            break

        while True:
            date = input("Date (d/m/y): ")  # Prompt for date in specified format
            try:
                date = datetime.strptime(date, "%d/%m/%Y").date()
                break
            except ValueError:
                print("Invalid check IN format. Please use 'd/m/y'.")

        Visits = c.Visits(name, country, gender, age_group, satis, date, self.trails)
        self.saveVisits(Visits.format())
        print(f"Client {name} Added.")
