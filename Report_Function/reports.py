# Import the datetime module to handle date operations
from datetime import datetime

class ActivityReport:
    def __init__(self):
        # Initialize an empty dictionary to hold data for each month/season
        self.data = {}

    def generate_report(self):
        # Define input and output file names
        input_file = 'clients.csv'
        output_file = 'reports.csv'

        try:
            # Step 1: Read and Process Input Data
            self.read_client_data(input_file)

            # Step 2: Generate Report
            report = self.create_monthly_report()

            # Step 3: Write Report to File
            self.write_report_to_file(report, output_file)

            # Print success message
            print("Report generated successfully.")

        except FileNotFoundError:
            # Handle case where input file is not found
            print(f"Error: The file '{input_file}' was not found.")
        except Exception as e:
            # Handle any other exceptions that might occur
            print(f"An error occurred: {e}")

    def read_client_data(self, input_file):
        # Open the input file for reading with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            next(file)  # Skip the header row if present
            # Iterate through each line in the file
            for line in file:
                # Split the line into fields using ';' as the delimiter and strip whitespace
                fields = line.strip().split(';')
                # Check if there are at least 6 fields to avoid index errors
                if len(fields) >= 6:
                    # Extract relevant information: name, satisfaction rating, and date
                    name = fields[0]  # Client's name
                    satisfaction = fields[4]  # Satisfaction rating
                    date = fields[5]  # Date of the entry
                    # Convert the date to a month string using the get_month method
                    month = self.get_month(date)
                    # Update the monthly data with the extracted information
                    self.update_monthly_data(month, name, satisfaction)

    def get_month(self, date_string):
        # Convert date string to datetime object and extract month
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%B')  # Return month name

    def update_monthly_data(self, month, name, satisfaction):
        # Initialize month data if it doesn't exist
        if month not in self.data:
            self.data[month] = {'clients': 0, 'satisfactions': []}

        # Add client name to set (ensures uniqueness) and satisfaction to list
        self.data[month]['clients'] += 1
        self.data[month]['satisfactions'].append(satisfaction)

    def create_monthly_report(self):
        # Initialize an empty list to store report entries
        report = []
        # Iterate through each month's data
        for month, info in self.data.items():
            num_visits = info['clients']
            ratings = info['satisfactions']
            # Create a report entry for each month
            report_entry = [
                month,
                num_visits,
                max(ratings, key=self.map_satisfaction) if ratings else None,
                min(ratings, key=self.map_satisfaction) if ratings else None,
                self.calculate_mode(ratings)
            ]
            report.append(report_entry)
        return report

    def write_report_to_file(self, report, output_file):
        # Open the output file and write the report
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write header
            file.write('Month;Number of Visits;Max Rating;Min Rating;Mode\n')
            # Write each report entry
            for entry in report:
                file.write(';'.join(map(str, entry)) + '\n')

    def calculate_mode(self, ratings):
        # Return None if the ratings list is empty
        if not ratings:
            return None

        # Count the frequency of each rating
        frequency_count = {}
        for rating in ratings:
            frequency_count[rating] = frequency_count.get(rating, 0) + 1

        # Find and return the mode (rating with highest frequency)
        mode = max(frequency_count, key=frequency_count.get)
        return mode

    def map_satisfaction(self, satisfaction):
        # Define a mapping of satisfaction ratings to numerical values
        mapping = {
            'Very Satisfied': 5,
            'Satisfied': 4,
            'Undecided': 3,
            'Unsatisfied': 2,
            'Very Unsatisfied': 1,
        }
        # Return the mapped value or 0 if not found
        return mapping.get(satisfaction, 0)
