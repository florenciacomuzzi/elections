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


def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except Exception as e:
        print(e)
        print("failed to send mail")


if __name__ == '__main__':
    send_email("", "", "", "t4st", "jhi")

    #
    # # Example usage
    # file_path = 'sample.csv'
    # data = read_csv_to_dict(file_path)
    #
    # amended = data
    # # Print the dictionary
    # for key, value in data.items():
    #     print(f"{key}: {value}")