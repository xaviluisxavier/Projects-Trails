import pandas as pd
import matplotlib.pyplot as plt

class ReportPlotter:
    def __init__(self):
        #Initialize with a fixed path to the CSV file
        self.filename = 'reports.csv'  # Fixed filename for the report

    def load_and_plot(self):
        #Load report data from the CSV file and plot the number of visits by country.
        try:
            # Load data from CSV
            data = pd.read_csv(self.filename, delimiter=';')

            # Check if the data is empty
            if data.empty:
                return  # Exit if there is no data to plot

            # Set up the plot
            plt.figure(figsize=(10, 6))

            # Create a bar chart for Number of Visits
            plt.bar(data['Country'], data['Number of Visits'], color='red')

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
        except pd.errors.EmptyDataError:
            print(f"Error: The file '{self.filename}' is empty.")
        except pd.errors.ParserError:
            print(f"Error: There was a problem parsing the file '{self.filename}'.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
