from matplotlib import pyplot as plt

class ReportsManager:
    def __init__(self, reports = 'reports.csv'):
        self.reports = reports  # Name of the CSV file containing report data

    def create_graph(self) -> None:
        try:
            # Initialize lists and variables to store data
            countries = []
            visits = []
            max_rating = None
            min_rating = None
            mode = None
            # Open and read the CSV file
            with open(self.reports, 'r', encoding='utf-8') as file:
                # Read the header line
                header = file.readline().strip().split(';')

                # Validate the header format
                if len(header) < 5 or header[0] != "Country" or header[1] != "Number of Visits" or \
                        header[2] != "Max Rating" or header[3] != "Min Rating" or header[4] != "Mode":
                    print("Error: The header of the file does not match the expected format.")
                    return

                # Process each line of the file
                for line in file:
                    if line.strip():  # Skip empty lines
                        data = line.strip().split(';')
                        countries.append(data[0])  # Add country name
                        visits.append(int(data[1]))  # Add number of visits

                        # Store rating data (only once)
                        if max_rating is None:
                            max_rating = data[2]
                        if min_rating is None:
                            min_rating = data[3]
                        if mode is None:
                            mode = data[4]

            # Check if there's enough data to create the graph
            if not countries or not visits:
                print("Not enough data to create the graph.")
                return

            # Create the plot
            plt.figure(figsize=(10, 6))
            bars = plt.bar(countries, visits, color='red', alpha=0.7)

            # Set title and labels
            plt.title('Number of Visits by Country')
            plt.xlabel('Country')
            plt.ylabel('Number of Visits')
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines

            # Add text annotations for ratings
            plt.text(0.75, 0.98, f'Max Rating: {max_rating}', transform=plt.gca().transAxes, verticalalignment='top')
            plt.text(0.75, 0.93, f'Min Rating: {min_rating}', transform=plt.gca().transAxes, verticalalignment='top')
            plt.text(0.75, 0.88, f'Mode: {mode}', transform=plt.gca().transAxes, verticalalignment='top')

            plt.tight_layout()  # Adjust layout to prevent clipping of labels
            plt.show()  # Display the plot

        except FileNotFoundError:
            print(f"Error: The file '{self.reports}' was not found.")
        except ValueError as e:
            print(f"Error: There was a problem converting data. {e}")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
