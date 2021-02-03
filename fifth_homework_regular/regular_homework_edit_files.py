import csv


def open_file(file_path):
    with open(file_path, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def write_data(data):
    with open("corrected_phonebook.csv", "w+") as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(data)
    return f


