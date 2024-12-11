class ActivityReport:
    def __init__(self):
        self.data = {}  # Dictionary to hold data for each country

    def generate_report(self):
        input_file = 'clients.csv'  # Input file name
        output_file = 'reports.csv'  # Output file name
        # Load data from the input file
        try:
            with open(input_file, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:  # Ensure the line is not empty
                        # Split the line into components
                        name, country, gender, age_group, satisfaction, date = line.split(';')
                        # Initialize country data if not already present
                        if country not in self.data:
                            self.data[country] = {
                                'clients': set(),  # Set to store unique client names
                                'satisfactions': []  # List to store satisfaction ratings
                            }

                        # Add client name and satisfaction rating
                        self.data[country]['clients'].add(name)
                        self.data[country]['satisfactions'].append(satisfaction)
            # Generate the report data
            report = []
            for country, info in self.data.items():
                num_visits = len(info['clients'])  # Count unique visitors
                ratings = info['satisfactions']

                # Determine max, min, and mode ratings
                max_rating = max(ratings, key=self.map_satisfaction) if ratings else None
                min_rating = min(ratings, key=self.map_satisfaction) if ratings else None
                mode_rating = self.calculate_mode(ratings)

                report.append([country, num_visits, max_rating, min_rating, mode_rating])

            print("Report generated successfully.")

            # Save the report to the output file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write('Country;Number of Visits;Max Rating;Min Rating;Mode\n')
                for entry in report:
                    file.write(';'.join(map(str, entry)) + '\n')
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_mode(self, ratings):

        if not ratings:
            return None  # Return None if there are no ratings available

        # Create a dictionary to count occurrences of each rating
        frequency_count = {}

        # Iterate through each rating in the list
        for rating in ratings:
            # Increment the count for this rating in the frequency dictionary
            frequency_count[rating] = frequency_count.get(rating, 0) + 1

        # Find the rating with the maximum frequency and return it as the mode
        mode = max(frequency_count.items(), key=lambda item: item[1])[0]
        return mode

    def map_satisfaction(self, satisfaction):

        # Define a mapping from satisfaction strings to numerical values
        mapping = {
            'Very Satisfied': 5,
            'Satisfied': 4,
            'Neutral': 3,
            'Unsatisfied': 2,
            'Very Unsatisfied': 1,
        }
        # Return the corresponding numeric value for the satisfaction level; default to 0 if not found
        return mapping.get(satisfaction, 0)
