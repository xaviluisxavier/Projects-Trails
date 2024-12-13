class ActivityReport:
    def __init__(self):
        # Initialize an empty dictionary to hold data for each country
        self.data = {}

    def generate_report(self):
        input_file = 'clients.csv'  # Name of the input file containing client data
        output_file = 'reports.csv'  # Name of the output file for the generated report
        # Load data from the input file
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()  # Remove any leading/trailing whitespace
                    if line:  # Ensure the line is not empty
                        # Split the line into components based on the delimiter ';'
                        name, country, gender, age_group, satisfaction, date = line.split(';')

                        # Initialize country data if it does not exist in the dictionary
                        if country not in self.data:
                            self.data[country] = {
                                'clients': set(),  # Set to store unique client names (no duplicates)
                                'satisfactions': []  # List to store satisfaction ratings
                            }
                        # Add client name and satisfaction rating to the respective country
                        self.data[country]['clients'].add(name)  # Add unique client name
                        self.data[country]['satisfactions'].append(satisfaction)  # Add satisfaction rating

            # Generate the report data
            report = []  # List to hold report entries
            for country, info in self.data.items():
                num_visits = len(info['clients'])  # Count unique visitors for this country
                ratings = info['satisfactions']  # Get satisfaction ratings for this country
                # Determine max, min, and mode ratings using helper functions
                max_rating = max(ratings, key=self.map_satisfaction) if ratings else None
                min_rating = min(ratings, key=self.map_satisfaction) if ratings else None
                mode_rating = self.calculate_mode(ratings)
                # Append the report entry for this country
                report.append([country, num_visits, max_rating, min_rating, mode_rating])
            print("Report generated successfully.")
            # Save the report to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                # Write the header for the report file
                file.write('Country;Number of Visits;Max Rating;Min Rating;Mode\n')
                for entry in report:
                    file.write(';'.join(map(str, entry)) + '\n')  # Write each entry as a new line
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' was not found.")  # Handle case where input file doesn't exist
        except Exception as e:
            print(f"An error occurred: {e}")  # Catch-all for any other exceptions

    def calculate_mode(self, ratings):
        if not ratings:  # If there are no ratings available
            return None  # Return None
        frequency_count = {}  # Dictionary to count occurrences of each rating
        for rating in ratings:  # Iterate through each rating in the list
            frequency_count[rating] = frequency_count.get(rating, 0) + 1  # Increment count for this rating
        # Find and return the rating with the maximum frequency (the mode)
        mode = max(frequency_count.items(), key=lambda item: item[1])[0]
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