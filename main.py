from Trails_Functions import trail_menu as mt

while True:
    print('\nMENU')
    print('1. Manage Trails')
    print('2. Manage Guides')
    print('3. Exit')

    while True:
        option = input('Enter your choice: ').strip()
        if option:
            try:
                option = int(option)
                if 1 <= option <= 3:
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
            print("Manage Guides functionality not implemented yet.")
        case 3:
            print("Exiting the program.")
            break