import csv


# Function that reads a CSV file and return a list of rows
def read_csv(file_path):
    rows = []
    with open(file_path, mode='r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            rows.append(row)
        return rows


# Function to find the difference between two CVS files
def find_difference(file1, file2):
    # Read contents of both said files
    csv1 = read_csv(file1)
    csv2 = read_csv(file2)

    # Find the rows in the file1 but not in the file2
    difference = [row for row in csv1 if row not in csv2]  # hmmmm

    return difference

#Paths to manually compare
file1_path = 'file1.csv'
file2_path = 'file2.csv'

diff = find_difference(file1_path, file2_path
                       )
#Print the different rows
if len(diff) > 0:
    print("Rows that are different:")
    for row in diff:
        print(row)
else:
    print("The CSV files are indifferent.")
