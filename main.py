# Import necessary modules for different functionalities
from Trails_Functions import trail_menu as mt
from Schedules_Functions import Schedules_manager as sm
from Guide_Functions import guide_menu as gm
from Clients_Functions import Clients_Manager as cm
from Report_Function import reports as rg
from Report_Function import graph as gh

# Main program loop
while True:
    # Display the main menu options
    print('\nMENU')
    print('1. Manage Trails')
    print('2. Manage Guides')
    print('3. Manage Clients')
    print('4. Manage Schedules')
    print('5. Reports')
    print('6. Generate Graph')
    print('7. Exit')

    # Input validation loop
    while True:
        option = input('Enter your choice: ').strip()
        if option:
            try:
                option = int(option)
                if 1 <= option <= 7:
                    break
                else:
                    print('Invalid option. Please choose between 1 and 7.')
            except ValueError:
                print('Invalid input. Please enter a number.')
        else:
            print('Input cannot be empty. Please enter a number.')

    # Match the user's choice to the corresponding function
    match option:
        case 1:
            mt.Trails_Menu()  # Manage Trails
        case 2:
            gm.Guides_Menu()  # Manage Guides
        case 3:
            cm.Clients_Manager().Create_Client()  # Manage Clients
        case 4:
            sm.SchedulesManager().CheckIn_and_Out()  # Manage Schedules
        case 5:
            rg.ActivityReport().generate_report()  # Generate Reports
        case 6:
            gh.ReportsManager().create_graph()  # Generate Graphs
        case 7:
            print("Exiting the program.")
            break  # Exit the program
