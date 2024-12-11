import json
from Guide_Functions import guide  # Import the guide class from the Guide_Functions module

g = guide  # Create an instance of the guide class

class Guide_Manager:
    @staticmethod
    def add_guide(filename: str):
        """Add a new guide to the specified file."""
        id = input("Enter guide's ID: ")  # Prompt user for the guide's ID
        with open(filename, 'r') as file:
            if id in file.read():  # Check if the ID already exists in the file
                print("ID already exists. Please try again.")  # Inform user if ID is duplicate
                return

        # Collect other details for the new guide
        name = input("Enter guide's name: ")  # Prompt for the guide's name
        experience = int(input("Enter experience (in years): "))  # Prompt for years of experience
        number = input("Enter the guide's phone number: ")  # Prompt for phone number
        email = input("Enter the guide's email: ")  # Prompt for email address
        languages = input("Enter languages (separated by ,): ").split(',')  # Prompt for languages
        availability = input("Enter availability (separated by ,): ").split(',')  # Prompt for availability

        # Create a new Guide instance with the collected information
        new_guide = g.Guide(id, name, experience, number, email,
                            [lang.strip() for lang in languages],  # Strip whitespace from language entries
                            [day.strip() for day in availability])  # Strip whitespace from availability entries

        # Load existing guides and add the new guide
        with open(filename, 'r') as file:
            guides_data = json.load(file)  # Load existing guides from JSON file

        guides_data.append(new_guide.__dict__)  # Append the new guide's dictionary representation to the list

        # Save changes back to the file
        with open(filename, 'w') as file:
            json.dump(guides_data, file, indent=4)  # Write updated list of guides back to JSON file

        print("Guide added successfully!")  # Confirm successful addition of the guide

    @staticmethod
    def remove_guide(filename: str):
        """Remove a guide from the specified file."""
        idAux = input("Enter the guide's id: ")  # Prompt user for the ID of the guide to remove

        with open(filename, 'r') as file:
            guides_data = json.load(file)  # Load existing guides from JSON file

        found = False  # Flag to check if the guide was found
        for guide in guides_data:  # Iterate through existing guides
            if guide['id'] == idAux:  # Check if current guide matches the provided ID
                found = True  # Set flag to indicate that a matching guide was found
                answer = input("Are you sure you want to remove this guide? (y/n) ")  # Confirm removal
                if answer.lower() == 'y':  # If user confirms removal
                    guides_data.remove(guide)  # Remove the guide from the list
                    with open(filename, 'w') as file:
                        json.dump(guides_data, file, indent=4)  # Save updated list back to JSON file
                    print("Guide removed successfully!")  # Confirm successful removal
                else:
                    print("Guide not removed.")  # Inform user that removal was canceled
                break

        if not found:  # If no matching guide was found
            print("Guide not found.")  # Inform user that no matching guide exists

    @staticmethod
    def view_guide(filename: str):
        """View details of guides."""
        print("\n1. View all guides")  # Option to view all guides
        print("2. View a specific guide")  # Option to view a specific guide by ID
        print("3. Back")  # Option to return to previous menu

        option = input("Choose an option: ")  # Prompt user for their choice

        if option == "1":  # If user wants to view all guides
            with open(filename, "r") as file:
                guides_data = json.load(file)  # Load existing guides from JSON file
            for guide in guides_data:
                print(json.dumps(guide, indent=4))  # Print each guide's details in a formatted way

        elif option == "2":  # If user wants to view a specific guide
            idAux = input("Enter the guide's ID that you want to see: ")
            with open(filename, "r") as file:
                guides_data = json.load(file)
            for guide in guides_data:
                if guide['id'] == idAux:
                    print(json.dumps(guide, indent=4))
                    break
            else:
                print("Guide not found")

        elif option == "3":
            return

        else:
            print("Invalid option. Try again.")

    @staticmethod
    def update_guide(filename: str):
        """Update details of an existing guide."""
        idAux = input("Enter the guide's ID that you want to update: ")

        with open(filename, 'r') as file:
            guides_data = json.load(file)

        found = False
        for guide in guides_data:
            if guide['id'] == idAux:
                found = True
                field_to_update = input(
                    "Enter what you want to update (id, experience, contact, languages, availability): ")

                if field_to_update not in ['id', 'experience', 'contact', 'languages', 'availability']:
                    print("Invalid field to update.")
                    continue

                if field_to_update == "id":
                    new_value = input("Enter the new ID: ")
                    if new_value in [g['id'] for g in guides_data]:
                        print("ID already exists. Please try again.")
                        continue
                    guide['id'] = new_value

                elif field_to_update == "experience":
                    new_value = int(input("Enter the new experience: "))
                    guide['experience'] = new_value

                elif field_to_update == "contact":
                    number = input("Enter the new number: ")
                    email = input("Enter the new email: ")
                    guide['contact']["number"] = number
                    guide['contact']["email"] = email

                elif field_to_update == "languages":
                    new_value = input("Enter the new languages (separated by ,): ").split(',')
                    guide['languages'] = [lang.strip() for lang in new_value]

                elif field_to_update == "availability":
                    new_value = input("Enter the new availability (separated by ,): ").split(',')
                    guide['availability'] = [day.strip() for day in new_value]

                with open(filename, 'w') as file:
                    json.dump(guides_data, file, indent=4)

                print("Guide updated successfully!")

        if not found:
            print("Guide not found.")
