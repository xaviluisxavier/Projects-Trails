import matplotlib.pyplot as plt


class ReportsManager:
    def __init__(self):
        self.filename = 'reports.csv'

    def create_graph(self):
        """Load report data from the CSV file and plot the number of visits by country."""
        try:
            countries = []  # List to hold country names
            visits = []  # List to hold number of visits

            # Load data from CSV
            with open(self.filename, 'r', encoding='utf-8') as file:
                # Read the header line
                header = file.readline().strip().split(';')

                # Check if header is correct
                if len(header) < 2 or header[0] != "Country" or header[1] != "Number of Visits":
                    print("Invalid CSV format.")
                    return

                # Read each subsequent line
                for line in file:
                    if line.strip():  # Ensure line is not empty
                        data = line.strip().split(';')  # Split line by semicolon
                        countries.append(data[0])  # First element is Country
                        visits.append(int(data[1]))  # Second element is Number of Visits

            # Check if the data is empty
            if not countries or not visits:
                print("No data to plot.")
                return

            # Set up the plot
            plt.figure(figsize=(10, 6))

            # Create a bar chart for Number of Visits
            plt.bar(countries, visits, color='red')

            # Add titles and labels
            plt.title('Number of Visits by Country')
            plt.xlabel('Country')
            plt.ylabel('Number of Visits')

            # Rotate x-axis labels for better visibility if necessary
            plt.xticks(rotation=45)

            # Show gridlines for better readability
            plt.grid(axis='y')

            # Show the plot
            plt.tight_layout()  # Adjust layout to make room for x labels
            plt.show()

        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except ValueError:
            print("Error: There was a problem converting data. Ensure that 'Number of Visits' contains valid integers.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

