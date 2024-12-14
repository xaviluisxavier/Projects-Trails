from Guide_Functions import guide_manager as gm

class Guides_Menu:
    def __init__(self):
        # Initialize the Guide_Manager object
        self.guide_manager = gm.Guide_Manager()

        # Main loop for the Guides Menu
        while True:
            # Display the menu options
            print('\n--- GUIDE MENU ---')
            print('1 - Create Guides')
            print('2 - Update Guide')
            print('3 - Remove Guides')
            print('4 - View Guide')
            print('5 - Back')

            # Input validation loop
            while True:
                option = input('Enter your choice: ').strip()
                if option:
                    try:
                        option = int(option)
                        if 1 <= option <= 5:
                            break  # Valid input, exit the validation loop
                        else:
                            print('Invalid option. Please choose a number between 1 and 5.')
                    except ValueError:
                        print('Invalid input. Please enter a number.')
                else:
                    print('Input cannot be empty. Please enter a number.')

            # Process the user's choice
            match option:
                case 1:
                    # Call the add_guide method to create a new guide
                    self.guide_manager.add_guide("guide.json")
                case 2:
                    # Call the update_guide method to modify an existing guide
                    self.guide_manager.update_guide("guide.json")
                case 3:
                    # Call the remove_guide method to delete a guide
                    self.guide_manager.remove_guide("guide.json")
                case 4:
                    # Call the view_guide method to display guide information
                    self.guide_manager.view_guide("guide.json")
                case 5:
                    # Exit the Guides Menu
                    break
        print("Returning to main menu")