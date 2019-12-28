# -*- coding: utf-8 -*-
from typing import Dict
from carleto.student.student import TemplateStudent, Role
from carleto.utils.build_roles_by_class import roles_by_class
from carleto.utils.build_students import build_students_from_csv, build_csv_output

facilitator = TemplateStudent("facilitator", Role.FACILITATOR)
facilitator.set_competences(3, 5, 4, 1, 2)

researcher = TemplateStudent("researcher", Role.RESEARCHER)
researcher.set_competences(3, 4, 1, 5, 2)

analyst = TemplateStudent("analyst", Role.ANALYST)
analyst.set_competences(4, 3, 1, 2, 5)

reviser = TemplateStudent("reviser", Role.REVISER)
reviser.set_competences(3, 1, 2, 5, 4)

support = TemplateStudent("support", Role.SUPPORT)
support.set_competences(5, 2, 4, 1, 3)

templates = [facilitator, researcher, analyst, reviser, support]

students = build_students_from_csv("utils/test_file.csv")
for student in students:
    student.calculate_score(templates)

room_classes = ["1A", "1B", "1C", "1D", "2A", "2B", "2C", "2D", "3A", "3B", "3C", "3D"]
rooms: Dict[str, dict] = dict()

for room in room_classes:
    rooms[room] = roles_by_class(students, room)

build_csv_output('teams_output.csv', rooms)
