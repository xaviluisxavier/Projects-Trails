from Guide_Functions import guide_manager as gm

class Guides_Menu:
    def __init__(self):
        self.guide_manager = gm.Guide_Manager()

        while True:
            print('1 - Create Guides')
            print('2 - Update Guide')
            print('3 - Remove Guides')
            print('4 - View Guide')
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
                    self.guide_manager.add_guide("guide.json")
                case 2:
                    self.guide_manager.update_guide("guide.json")
                case 3:
                    self.guide_manager.remove_guide("guide.json")
                case 4:
                    self.guide_manager.view_guide("guide.json")
                case 5:
                    break
        print("Returning to main menu")