from Trails_Functions import trail_menu as mt


while True:
    print('\nMENU')
    print('1. Manage Trails')
    print('2. Manage Guides')
    print('3. Exit')
    option = int(input('Enter your choice: '))
    if 0 <= option <= 3:
        match option:
            case 1:
                mt.Trails_Menu()
            case 2:
                pass
            case 3:
                break
    else:
        print('Invalid option')