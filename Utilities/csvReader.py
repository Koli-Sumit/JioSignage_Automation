import csv

# Open the CSV file
file_path = r'C:\Users\shivaji.ghadage\PycharmProjects\JB_CMS\SampleData\csv_sample.csv'
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # Assuming the CSV file has headers

    # Retrieve column values
    column_values_name = []
    column_values_serial = []
    column_values_group = []
    column_name = 'Name'
    column_serial = 'Serial Number'
    column_group = 'Group Name'

    for row in reader:
        column_values_name.append(row[column_name])
        column_values_serial.append(row[column_serial])
        column_values_group.append(row[column_group])

# Printing the retrieved column values
print(column_values_name)
print(column_values_serial)
print(column_values_group)