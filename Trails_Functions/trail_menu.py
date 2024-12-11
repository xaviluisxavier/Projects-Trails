from Trails_Functions import trail_manager as tm

class Trails_Menu:
    def __init__(self):
        self.trail_manager = tm.TrailManager()  # Create an instance of TrailManager

        while True:
            print('1 - Create Trail')
            print('2 - Update Trails')
            print('3 - Remove Trails')
            print('4 - View Trail')
            print('5 - Back')

            while True:
                option = input('Enter your choice: ').strip()
                if option:
                    try:
                        option = int(option)
                        if 1 <= option <= 5:
                            break
                        else:
                            print('Invalid option. Please choose a number between 1 and 5.')
                    except ValueError:
                        print('Invalid input. Please enter a number.')
                else:
                    print('Input cannot be empty. Please enter a number.')

            match option:
                case 1:
                    self.trail_manager.create_Trail()
                case 2:
                    self.trail_manager.Edit_Trail()
                case 3:
                    self.trail_manager.remove_Trail()
                case 4:
                    self.trail_manager.show_Trail()
                case 5:
                    break

        print("Returning to main menu.")  # Feedback when exiting the Trails Menu