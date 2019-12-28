from typing import Dict, List
from carleto.student.student import Student, Role


def roles_by_class(students: list, room_class: str) -> dict:
    roles: Dict[Role, List[Student]] = {Role.FACILITATOR: [],
                                        Role.RESEARCHER: [],
                                        Role.ANALYST: [],
                                        Role.REVISER: [],
                                        Role.SUPPORT: []}

    searching = True
    highest_score = 15
    while searching:
        for student in students:
            if student.room_class == room_class:
                for role in student.scores:
                    if student.scores[role] == highest_score and not student.used and len(roles[role]) < 9:
                        student.used = True
                        roles[role].append(student)
        highest_score -= 1
        if highest_score < 3:
            searching = False

    return roles
