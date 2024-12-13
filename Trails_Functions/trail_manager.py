from Trails_Functions import trail  # Import the trail class from the Trails_Functions module

t = trail  # Create an instance of the trail class

class TrailManager:
    def __init__(self, tf="trails.csv"):
        #Initialize the TrailManager with file names for trails and schedules.
        self.trail = tf  # Set the filename for trails

    def save_Trails(self, trail):
        #Append a new trail entry to the trails file.
        with open(self.trail, "a", encoding="utf-8") as file:
            file.write(trail + '\n')  # Write the trail entry followed by a newline for proper CSV formatting

    def create_Trail(self):
        #Collect information to create a new trail and save it.
        print("\n--- Create New Trail ---")  # Header for creating a new trail
        diff_list = {"1": "Easy", "2": "Medium", "3": "Hard"}  # Difficulty levels mapping
        ext_list = {"1": "0-5km", "2": "5-10km", "3": "10-15km", "4": "15-30km",
                    "5": "+30km"}  # Trail extensions mapping
        form_list = {"1": "Circular", "2": "Linear"}  # Trail forms mapping

        while True:
            id_input = input('Trail ID -> ').strip()  # Prompt for trail ID
            if not id_input:
                print("ID cannot be empty. Please try again.")  # Validate input
                continue
            try:
                id = int(id_input)  # Convert input to an integer
                break  # Exit loop if conversion is successful
            except ValueError:
                print("ID must be a number. Please try again.")  # Handle non-integer input

        while True:
            name = input('Trail name -> ').strip()  # Prompt for trail name
            if not name:
                print('Name cannot be empty. Please enter a valid trail name.')  # Validate input
                continue
            break

        while True:
            island = input('Island -> ').strip()  # Prompt for island name
            if not island:
                print('Island cannot be empty. Please enter a valid island name.')  # Validate input
                continue
            break

        while True:
            council = input('Municipal Council -> ').strip()  # Prompt for municipal council name
            if not council:
                print('Council cannot be empty. Please enter a valid council name.')  # Validate input
                continue
            break

        while True:
            coordinates = input('GPS Coordinates -> ').strip()  # Prompt for GPS coordinates
            if not coordinates:
                print('Coordinates cannot be empty. Please enter valid GPS coordinates.')  # Validate input
                continue
            break

        while True:
            choice = input(
                "Insert the Difficulty (1.Easy, 2.Medium, 3.Hard) -> ").strip()  # Prompt for difficulty level
            if choice not in diff_list:
                print("Invalid difficulty. Please try again.")
                continue
            difficulty = diff_list[choice]  # Get corresponding difficulty from dictionary
            break

        while True:
            print("Extension: 1. 0-5km, 2. 5-10km, 3. 10-15km, 4. 15-30km, 5. +30km")
            choice = input("Insert the number corresponding to the extension -> ").strip()
            if choice not in ext_list:
                print("Invalid extension. Please try again.")
                continue
            extension = ext_list[choice]
            break

        while True:
            choice = input("Insert the Form (1. Circular, 2. Linear) -> ").strip()
            if choice not in form_list:
                print("Invalid form. Please try again.")
                continue
            form = form_list[choice]
            break

        while True:
            description = input('Brief description -> ').strip()  # Prompt for a brief description of the trail
            if not description:
                print('Description cannot be empty. Please enter a valid description.')  # Validate input
                continue
            break
        # Create an instance of Trails and save it using the collected information
        trail_instance = t.Trails(id, name, island, council, coordinates, difficulty, extension, form, description)
        self.save_Trails(trail_instance.format())  # Save the formatted trail entry to the CSV file
        print(f"Trail: {name} with the ID: {id} created successfully")  # Confirm successful creation of the trail

    def remove_Trail(self):
        #Remove a trail by its ID.
        while True:
            id_input = input('Trail ID to remove -> ').strip()  # Prompt for ID of the trail to remove
            if not id_input:
                print("ID cannot be empty. Please try again.")
                continue
            try:
                id = int(id_input)
                break
            except ValueError:
                print("ID must be a number. Please try again.")

        with open(self.trail, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(self.trail, "w", encoding="utf-8") as file:
            for line in lines:
                if str(id) != line.strip().split(";")[0]:
                    file.write(line)
                else:
                    trail_found = True
        if trail_found:
            print(f"Trail with ID: {id} removed successfully.")
        else:
            print(f"No trail found with ID: {id}.")

    def Edit_Trail(self):
        # Edit details of an existing trail
        while True:
            # Prompt user for the Trail ID to edit
            id_input = input('Trail ID to edit -> ').strip()
            if not id_input:
                print("ID cannot be empty. Please try again.")
                continue
            try:
                # Convert input to integer
                id = int(id_input)
                break
            except ValueError:
                print("ID must be a number. Please try again.")

        # Open and read the trail file
        with open(self.trail, "r", encoding="utf-8") as file:
            lines = file.readlines()
        trail_found = False

        # Iterate through each line in the file
        for i, line in enumerate(lines):
            # Check if the current line's ID matches the input ID
            if str(id) == line.split(";")[0]:
                trail_found = True
                # Split the line into individual data fields
                trail_data = line.strip().split(";")

                # Display current details of the found trail
                print("\nCurrent trail details:")
                print(f"1. Name: {trail_data[1]}")
                print(f"2. Island: {trail_data[2]}")
                print(f"3. Council: {trail_data[3]}")
                print(f"4. Coordinates: {trail_data[4]}")
                print(f"5. Difficulty: {trail_data[5]}")
                print(f"6. Extension: {trail_data[6]}")
                print(f"7. Form: {trail_data[7]}")
                print(f"8. Description: {trail_data[8]}")

                while True:
                    # Prompt user to choose which field to edit
                    choice = input("Enter the number of the field to edit (1-8): ").strip()
                    if choice in ['1', '2', '3', '4', '5', '6', '7', '8']:
                        field_index = int(choice)
                        while True:
                            if field_index == 5:  # Field "Difficulty"
                                # Display difficulty options
                                print("\nChoose difficulty:")
                                print("1 - Easy")
                                print("2 - Medium")
                                print("3 - Hard")
                                difficulty_choice = input("Enter your choice (1-3): ").strip()
                                difficulty_map = {"1": "Easy", "2": "Medium", "3": "Hard"}
                                new_value = difficulty_map.get(difficulty_choice)
                                if new_value:
                                    break
                                else:
                                    print("Invalid choice. Please try again.")
                            elif field_index == 6:  # Field "Extension"
                                # Display extension options
                                print("\nChoose extension:")
                                print("1 - 0-5km")
                                print("2 - 5-10km")
                                print("3 - 10-15km")
                                print("4 - 15-30km")
                                print("5 - +30km")
                                extension_choice = input("Enter your choice (1-5): ").strip()
                                extension_map = {"1": "0-5km", "2": "5-10km", "3": "10-15km", "4": "15-30km",
                                                 "5": "+30km"}
                                new_value = extension_map.get(extension_choice)
                                if new_value:
                                    break
                                else:
                                    print("Invalid choice. Please try again.")
                            else:  # Other fields
                                # For other fields, allow free text input
                                new_value = input("Enter new value: ").strip()
                                if new_value:
                                    break
                                else:
                                    print("Value cannot be empty. Please try again.")

                        # Update the selected field with the new value
                        trail_data[field_index] = new_value
                        # Reconstruct the line with updated data
                        lines[i] = ";".join(trail_data) + "\n"

                        # Write all updated lines back to the file
                        with open(self.trail, "w", encoding="utf-8") as file:
                            file.writelines(lines)

                        print(f"Trail with ID: {id} updated successfully.")
                        return  # Exit after updating
                    else:
                        print("Invalid choice. Please enter a number between 1 and 8.")

        # If loop completes without finding the trail
        if not trail_found:
            print("No trail found with this ID. Please try again.")

    def show_Trail(self):
        #Display details of a specific trail by its ID.
        id = input("Enter the ID of the Trail you want to view: ")
        with open(self.trail, "r", encoding="utf-8") as file:
            lines = file.readlines()  # Read all lines from trails file
            trail_found = False  # Flag to check if the specified trail was found
            for line in lines:  # Iterate through each line (trail)
                if line.split(";")[0] == id:  # Check if current line matches specified ID
                    # Print details of the found trail in a formatted manner
                    print(f"ID -> {line.strip().split(';')[0]}")
                    print(f"Name -> {line.strip().split(';')[1]}")
                    print(f"Location -> {line.strip().split(';')[2]}")
                    print(f"Council -> {line.strip().split(';')[3]}")
                    print(f"Coordinates -> {line.strip().split(';')[4]}")
                    print(f"Difficulty -> {line.strip().split(';')[5]}")
                    print(f"Extension -> {line.strip().split(';')[6]}")
                    print(f"Form -> {line.strip().split(';')[7]}\n\n")
                    trail_found = True  # Set flag indicating that a matching trail was found
                    break
            if not trail_found:  # If no matching trails were found after iterating through all lines
                print(f"No Trail found with ID: {id}")  # Inform user that no matching ID exists.
