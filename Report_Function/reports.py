class ReportGenerator:
    def __init__(self, filename="schedule.csv"):
        self.filename = filename

    def generate_report(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                satisfactions = []

                for line in file:
                    row = line.strip().split(";")  # Split the line by the delimiter
                    if len(row) > 5:  # Ensure there are enough columns
                        satisfaction = int(row[5])  # Assuming satisfaction is the sixth column
                        satisfactions.append(satisfaction)

                if not satisfactions:
                    print("No data available for report.")
                    return

                total_visits = len(satisfactions)
                max_satisfaction = max(satisfactions)
                min_satisfaction = min(satisfactions)

                # Calculate mode
                mode_satisfaction = max(set(satisfactions), key=satisfactions.count)

                print(f"Total Visits: {total_visits}")
                print(f"Max Satisfaction: {max_satisfaction}")
                print(f"Min Satisfaction: {min_satisfaction}")
                print(f"Mode Satisfaction: {mode_satisfaction}")

        except FileNotFoundError:
            print("The file does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
