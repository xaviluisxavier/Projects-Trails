import json
from Guide_Functions import guide

class Guide_Manager:
    @staticmethod
    def add_guide(filename: str):
        id = input("Enter guide's ID: ")
        with open(filename, 'r') as file:
            if id in file.read():
                print("ID already exists. Please try again.")
                return

        name = input("Enter guide's name: ")
        experience = int(input("Enter experience (in years): "))
        number = input("Enter the guide's phone number: ")
        email = input("Enter the guide's email: ")
        languages = input("Enter languages (separated by ,): ").split(',')
        availability = input("Enter availability (separated by ,): ").split(',')

        # Create a new Guide instance
        new_guide = Guide(id, name, experience, number, email,
                          [lang.strip() for lang in languages],
                          [day.strip() for day in availability])

        # Load existing guides and add the new guide
        with open(filename, 'r') as file:
            guides_data = json.load(file)

        guides_data.append(new_guide.__dict__)

        # Save changes back to the file
        with open(filename, 'w') as file:
            json.dump(guides_data, file, indent=4)

        print("Guide added successfully!")

    @staticmethod
    def remove_guide(filename: str):
        idAux = input("Enter the guide's id: ")

        with open(filename, 'r') as file:
            guides_data = json.load(file)

        found = False
        for guide in guides_data:
            if guide['id'] == idAux:
                found = True
                answer = input("Are you sure you want to remove this guide? (y/n) ")
                if answer.lower() == 'y':
                    guides_data.remove(guide)
                    with open(filename, 'w') as file:
                        json.dump(guides_data, file, indent=4)
                    print("Guide removed successfully!")
                else:
                    print("Guide not removed.")
                break

        if not found:
            print("Guide not found.")

    @staticmethod
    def view_guide(filename: str):
        print("\n1. View all guides")
        print("2. View a specific guide")
        print("3. Back")

        option = input("Choose an option: ")

        if option == "1":
            with open(filename, "r") as file:
                guides_data = json.load(file)
            for guide in guides_data:
                print(json.dumps(guide, indent=4))

        elif option == "2":
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

                # Save changes back to the file
                with open(filename, 'w') as file:
                    json.dump(guides_data, file, indent=4)

                print("Guide updated successfully!")

        if not found:
            print("Guide not found.")