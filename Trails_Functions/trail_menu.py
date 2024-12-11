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
            option = int(input('Enter your choice: '))
            if 0 < option < 6:
                match option:
                    case 1:
                        self.trail_manager.create_Trail()  # Call create_Trail on the instance
                    case 2:
                        self.trail_manager.Edit_Trail()
                    case 3:
                        self.trail_manager.remove_Trail()
                    case 4:
                        self.trail_manager.show_Trail()
                    case 5:
                        break
            else:
                print("Invalid option. Please try again.")  # Provide feedback for invalid options

