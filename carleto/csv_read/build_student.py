# -*- coding: utf-8 -*-

import csv
from typing import List

from carleto.student.student import Student, Competence

students: List[Student] = []

with open("test_file.csv", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        s = Student(row["Nome"])

        communication = row["Quais são suas habilidades mais fortes? [Comunicação]"]
        organization = row["Quais são suas habilidades mais fortes? [Organização]"]
        empathy = row["Quais são suas habilidades mais fortes? [Empatia]"]
        curiosity = row["Quais são suas habilidades mais fortes? [Curiosidade]"]
        interpretation = row["Quais são suas habilidades mais fortes? [Interpretação]"]

        s.set_competences(communication, organization, empathy, curiosity, interpretation)

        students.append(s)

for s in students:
    print(s.name)
    print(s.competences[Competence.COMMUNICATION])
