from fileinput import filename

from ex1 import Person


def modifier(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    people = []
    for line in lines[1:]:
        fields = line.strip().split(',')
        surname = fields[0]
        first_name = fields[1]
        nickname = fields[2] if len(fields) > 2 else None
        birth_date_str = fields[3] if len(fields) > 3 else None
        person = Person (surname, first_name, nickname, birth_date_str)
        people.append(person)

    modified_lines = [lines[0].strip() + ',fullname,age\n']
    for person in people:
        fullname = person.get_fullname()
        age = person.get_age()
        modified_line = f"{person.surname},{person.first_name},{person.nickname or ''},{person.birth_date or ''},{fullname},{age}\n"
        modified_lines.append(modified_line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)

# Виконання другого завдання
modifier (filename)