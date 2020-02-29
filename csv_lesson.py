import csv


def csv_lesson():
    users = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]
    fields = ['name', 'age', 'job']
    with open('export.csv', 'w', encoding='utf-8', newline='') as users_list:
        writer = csv.DictWriter(users_list, fields, delimiter=';')
        writer.writeheader()
        for user in users:
            writer.writerow(user)


if __name__ == '__main__':
    csv_lesson()
