# -*- coding: utf-8 -*-

import csv
from carleto.student.student import Student


def build_students_from_csv(csv_source: str) -> list:
    students = []

    with open(csv_source, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            student = Student(row["Nome"])
            student.set_class(row["Turma"])

            communication = row["Quais são suas habilidades mais fortes? [Comunicação]"]
            organization = row["Quais são suas habilidades mais fortes? [Organização]"]
            empathy = row["Quais são suas habilidades mais fortes? [Empatia]"]
            curiosity = row["Quais são suas habilidades mais fortes? [Curiosidade]"]
            interpretation = row["Quais são suas habilidades mais fortes? [Interpretação]"]

            student.set_competences(communication, organization, empathy, curiosity, interpretation)

            students.append(student)
    return students


def build_csv_output(file_output: str, rooms: dict):
    with open(file_output, 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['NAME', 'CLASS', 'ROLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for room in rooms:
            print('>>', room)
            for role in rooms[room]:
                for student in rooms[room][role]:
                    print(student.name, room, role.name)
                    writer.writerow({'NAME': student.name, 'CLASS': room, 'ROLE': role.name})
