class ActivityReport:
    def __init__(self):
        # Initialize an empty dictionary to hold data for each country
        self.data = {}

    def generate_report(self):
        #Main function to generate the report from client data.
        #Reads input, processes data, and writes the report to a file.
        input_file = 'clients.csv'
        output_file = 'reports.csv'

        try:
            # Step 1: Read and Process Input Data
            self.read_client_data(input_file)

            # Step 2: Generate Report
            report = self.create_country_report()

            # Step 3: Write Report to File
            self.write_report_to_file(report, output_file)

            print("Report generated successfully.")

        except FileNotFoundError:
            print(f"Error: The file '{input_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Reads client data from the input file and processes each line.
    def read_client_data(self, input_file):
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():  # Ignore empty lines
                    # Split the line and extract relevant information
                    name, country, _, _, satisfaction, _ = line.strip().split(';')
                    self.update_country_data(country, name, satisfaction)

    # Updates the data structure with client information for each country.
    def update_country_data(self, country, name, satisfaction):
        # Initialize country data if it doesn't exist
        if country not in self.data:
            self.data[country] = {'clients': set(), 'satisfactions': []}

        # Add client name to set (ensures uniqueness) and satisfaction to list
        self.data[country]['clients'].add(name)
        self.data[country]['satisfactions'].append(satisfaction)

    # Generates the report data for each country.
    def create_country_report(self):
        report = []
        for country, info in self.data.items():
            num_visits = len(info['clients'])
            ratings = info['satisfactions']
            report_entry = [
                country,
                num_visits,
                max(ratings, key=self.map_satisfaction) if ratings else None,
                min(ratings, key=self.map_satisfaction) if ratings else None,
                self.calculate_mode(ratings)
            ]
            report.append(report_entry)
        return report

    # Writes the generated report to the output file.
    def write_report_to_file(self, report, output_file):
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write header
            file.write('Country;Number of Visits;Max Rating;Min Rating;Mode\n')
            # Write each report entry
            for entry in report:
                file.write(';'.join(map(str, entry)) + '\n')

    def calculate_mode(self, ratings):
        # Check if ratings list is empty
        if not ratings:
            return None

        # Count the frequency of each rating
        frequency_count = {}
        for rating in ratings:
            if rating in frequency_count:
                frequency_count[rating] += 1
            else:
                frequency_count[rating] = 1

        # Find the rating with the highest frequency
        mode = None
        max_frequency = 0
        for rating, count in frequency_count.items():
            if count > max_frequency:
                mode = rating
                max_frequency = count
        return mode

    def map_satisfaction(self, satisfaction):
        # Define a mapping from satisfaction strings to numerical values
        mapping = {
            'Very Satisfied': 5,
            'Satisfied': 4,
            'Undecided': 3,
            'Unsatisfied': 2,
            'Very Unsatisfied': 1,
        }
        # Return the corresponding numeric value for the satisfaction level; default to 0 if not found
        return mapping.get(satisfaction, 0)