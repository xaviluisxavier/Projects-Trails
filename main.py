from Trails_Functions import trail_menu as mt
from Schedules_Functions import Schedules_manager as sm
from Guide_Functions import guide_menu as gm
from Clients_Functions import Clients_Manager as cm

while True:
    print('\nMENU')
    print('1. Manage Trails')
    print('2. Manage Guides')
    print('3. Manage Schedules')
    print('4. Manage Clients')
    print('5. Exit')

    while True:
        option = input('Enter your choice: ').strip()
        if option:
            try:
                option = int(option)
                if 1 <= option <= 5:
                    break
                else:
                    print('Invalid option. Please choose 1, 2, or 3.')
            except ValueError:
                print('Invalid input. Please enter a number.')
        else:
            print('Input cannot be empty. Please enter a number.')
    match option:
        case 1:
            mt.Trails_Menu()
        case 2:
            gm.Guides_Menu()
        case 3:
            sm.SchedulesManager().CheckIn_and_Out()
        case 4:
            cm.Clients_Manager().Create_Client()
        case 5:
            print("Exiting the program.")
            break