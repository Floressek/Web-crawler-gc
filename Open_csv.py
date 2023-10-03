import csv

# Define the path to your CSV file
csv_file_path = 'products.csv'  # Replace 'your_file.csv' with the actual file path

try:
    with open(csv_file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Read and display the header row (if it exists)
        header = next(reader)
        if header:
            print("Header:", header)

        # Read and display each row of data
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"File '{csv_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")