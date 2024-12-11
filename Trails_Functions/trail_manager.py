from Trails_Functions import trail
# tf = trail file
# st = save file
t = trail


class TrailManager:
    def __init__(self,tf = "trails.csv", st = trail):
        self.trail = tf
        self.trails = st

    def save_Trails(self,st):
        with open(self.trail, "a", encoding="utf-8") as file:
            file.write(st + '\n')

    def create_Trail(self):
        print("\n--- Create New Trail ---")
        diff_list = {
            "1": "Easy",
            "2": "Medium",
            "3": "Hard"
        }
        ext_list = {
            "1": "0-5km",
            "2": "5-10km",
            "3": "10-15km",
            "4": "15-30km",
            "5": "+30km"
        }
        form_list = {
            "1":"Circular",
            "2":"Linear"
        }

        while True:
            id = int(input('Trail ID -> ').strip())
            if not id:
                print("ID cannot be empty. Please try again.")
                continue
            break

        while True:
            name = input('Trail name -> ').strip()
            if not name:
                print('Name cannot be empty. Please enter a valid trail name.')
                continue  # Ask for input again
            break

        while True:
            island = input('Island -> ').strip()
            if not island:
                print('Island cannot be empty. Please enter a valid island name.')
                continue  # Ask for input again
            break

        while True:
            council = input('Municipal Council -> ').strip()
            if not council:
                print('Council cannot be empty. Please enter a valid council name.')
                continue  # Ask for input again
            break

        while True:
            coordinates = input('GPS Coordinates -> ').strip()
            if not coordinates:
                print('Coordinates cannot be empty. Please enter valid GPS coordinates.')
                continue  # Ask for input again
            break

        while True:
            choice = input("Insert the Difficulty (1.Easy, 2.Medium, 3.Hard) -> ").title()
            if choice not in diff_list:
                print("Invalid difficulty. Please try again.")
                continue  # Ask for input again
            difficulty = diff_list[choice]
            break

        while True:
            print("Extension: 1. 0-5km, 2. 5-10km, 3. 10-15km, 4. 15-30km, 5. +30km")
            choice = input("Insert the number corresponding to the extension -> ")
            if choice not in ext_list:
                print("Invalid extension. Please try again.")
                continue  # Ask for input again
            extension = ext_list[choice]
            break

        while True:
            choice = input("Insert the Form (1. Circular, 2. Linear) -> ").title()
            if choice not in form_list:
                print("Invalid form. Please try again.")
                continue  # Ask for input again
            form = form_list[choice]
            break

        while True:
            description = input('Brief description -> ').strip()
            if not description:
                print('Description cannot be empty. Please enter a valid description.')
                continue  # Ask for input again
            break

        # Create an instance of Trails and save it
        trail_instance = t.Trails(id, name, island, council, coordinates, difficulty, extension, form, description)
        self.save_Trails(trail_instance.format())
        print(f"Trail: {name} with the ID: {id} created successfully")

    def remove_Trail(self):
        while True:
            id = int(input('Trail ID -> ').strip())
            break
        with open(self.trail, "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open(self.trail, "w", encoding="utf-8") as file:
            for line in lines:
                if str(id) != line.strip().split(";")[0]:
                    file.write(line)
        print(f"Trail with ID: {id} removed ")

    def Edit_Trail(self):
        while True:
            id = input('Trail ID to edit -> ').strip()
            with open(self.trail, "r", encoding="utf-8") as file:
                lines = file.readlines()
            # Check if the trail exists
            for i, line in enumerate(lines):
                if str(id) == line.split(";")[0]:
                    trail_data = line.strip().split(";")
                    print("\nCurrent trail details:")
                    print(f"1. Name: {trail_data[1]}")
                    print(f"2. Island: {trail_data[2]}")
                    print(f"3. Council: {trail_data[3]}")
                    print(f"4. Coordinates: {trail_data[4]}")
                    print(f"5. Difficulty: {trail_data[5]}")
                    print(f"6. Extension: {trail_data[6]}")
                    print(f"7. Form: {trail_data[7]}")
                    print(f"8. Description: {trail_data[8]}")
                    # Allow the user to edit a field
                    choice = input("Enter the number of the field to edit (1-8): ")
                    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                        new_value = input("Enter new value: ").strip()
                        if new_value:
                            trail_data[int(choice)] = new_value  # Update the field
                            lines[i] = ";".join(trail_data) + "\n"  # Update the line in the file
                            with open(self.trail, "w", encoding="utf-8") as file:
                                file.writelines(lines)  # Write all lines back to the file
                            print(f"Trail with ID: {id} updated successfully.")
                            return  # Exit the function after updating
                        else:
                            print("Value cannot be empty.")
                    else:
                        print("Invalid choice.")
            print("No trail found with this ID. Please try again.")

    def show_Trail(self):
        id = input("Enter the ID of the Trail you want to view: ")
        with open(self.trail, "r", encoding="utf-8") as file:
            lines = file.readlines()
            trail_found = False
            for line in lines:
                if line.split(";")[0] == id:
                    print(f"ID -> {line.strip().split(';')[0]}")
                    print(f"Name -> {line.strip().split(';')[1]}")
                    print(f"Location -> {line.strip().split(';')[2]}")
                    print(f"Council -> {line.strip().split(';')[3]}")
                    print(f"Coordinates -> {line.strip().split(';')[4]}")
                    print(f"Difficulty -> {line.strip().split(';')[5]}")
                    print(f"Extension -> {line.strip().split(';')[6]}")
                    print(f"Form -> {line.strip().split(';')[7]}\n\n")
                    trail_found = True
                    break
            if not trail_found:
                print(f"No Trail found with ID: {id}")
