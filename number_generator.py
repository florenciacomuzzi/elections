import csv


def read_csv_to_dict(file_path):
    data_dict = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Initialize the dictionary with empty lists for each header
        for header in reader.fieldnames:
            data_dict[header] = []

        # Populate the dictionary with data from each row
        for row in reader:
            for header in reader.fieldnames:
                data_dict[header].append(row[header])

    return data_dict


if __name__ == '__main__':
    # Example usage
    file_path = 'sample.csv'
    data = read_csv_to_dict(file_path)

    # Print the dictionary
    for key, value in data.items():
        print(f"{key}: {value}")