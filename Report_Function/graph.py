from matplotlib import pyplot as plt  # Importing the pyplot module from matplotlib for plotting graphs

class ReportsManager:
    def __init__(self, reports='reports.csv'):
        self.reports = reports  # Initialize the class with the name of the CSV file containing report data

    def create_graph(self) -> None:
        try:
            # Initialize lists and variables to store data
            countries = []  # List to hold country names
            visits = []     # List to hold number of visits corresponding to each country
            max_rating = None  # Variable to store the maximum rating (initialized to None)
            min_rating = None  # Variable to store the minimum rating (initialized to None)
            mode = None        # Variable to store the mode (initialized to None)

            # Open and read the CSV file
            with open(self.reports, 'r', encoding='utf-8') as file:
                # Read the header line from the CSV file and split it into a list
                header = file.readline().strip().split(';')

                # Validate the header format to ensure it matches expected columns
                if len(header) < 5 or header[0] != "Country" or header[1] != "Number of Visits" or \
                        header[2] != "Max Rating" or header[3] != "Min Rating" or header[4] != "Mode":
                    print("Error: The header of the file does not match the expected format.")
                    return  # Exit if header validation fails

                # Process each line of the file (after the header)
                for line in file:
                    if line.strip():  # Skip empty lines
                        data = line.strip().split(';')  # Split line into individual data fields
                        countries.append(data[0])  # Add country name to countries list
                        visits.append(int(data[1]))  # Convert number of visits to int and add to visits list

                        # Store rating data
                        if max_rating is None:  # If max_rating hasn't been set yet
                            max_rating = data[2]  # Set max_rating from data
                        if min_rating is None:  # If min_rating hasn't been set yet
                            min_rating = data[3]  # Set min_rating from data
                        if mode is None:        # If mode hasn't been set yet
                            mode = data[4]      # Set mode from data

            # Check if there's enough data to create the graph
            if not countries or not visits:  # If either list is empty
                print("Not enough data to create the graph.")
                return  # Exit if there isn't enough data

            # Create the plot using matplotlib
            plt.figure(figsize=(10, 6))  # Set the figure size for the plot
            plt.bar(countries, visits, color='red', alpha=0.7)  # Create a bar chart

            # Set title and labels for the plot
            plt.title('Number of Visits by Country')
            plt.xlabel('Country')
            plt.ylabel('Number of Visits')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines for better visualization

            # Add text annotations for ratings on the plot
            plt.text(0.75, 0.98, f'Max Rating: {max_rating}', transform=plt.gca().transAxes, verticalalignment='top')
            plt.text(0.75, 0.93, f'Min Rating: {min_rating}', transform=plt.gca().transAxes, verticalalignment='top')
            plt.text(0.75, 0.88, f'Mode: {mode}', transform=plt.gca().transAxes, verticalalignment='top')

            plt.tight_layout()  # Adjust layout to prevent clipping of labels and elements in the plot
            plt.show()         # Display the plot on screen

        except FileNotFoundError:
            print(f"Error: The file '{self.reports}' was not found.")  # Handle case where the file does not exist
        except ValueError as err:
            print(f"Error: There was a problem converting data. {err}")  # Handle conversion errors
        except Exception as err:
            print(f"An error occurred while loading data: {err}")  # Catch-all for any other exceptions that may occur