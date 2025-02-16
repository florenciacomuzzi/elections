import random
import csv


if __name__ == '__main__':
    # Step 1: Generate a list of random numbers
    random_numbers = [random.randint(1, 100) for _ in
                      range(10)]  # Generates 10 random numbers between 1 and 100

    # Step 2: Write the list to a CSV file
    with open('random_numbers.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Random Numbers"])  # Write a header (optional)
        writer.writerow(random_numbers)  # Write the list of random numbers

    # Step 3: Print the list of random numbers (optional)
    print("Random Numbers:", random_numbers)
    print("CSV file 'random_numbers.csv' has been created.")
