from carleto.student.student import Student, Role


def roles_by_class(students: list, room_class: str):
    student: Student

    roles = {Role.FACILITATOR: [],
             Role.RESEARCHER: [],
             Role.ANALYST: [],
             Role.REVISER: [],
             Role.SUPPORT: []}

    searching = True
    highest_score = 15
    count = 0
    while searching:
        for student in students:
            if student.room_class == room_class:
                for score in student.score:
                    if student.score[score] == highest_score and student.used is False:
                        if len(roles[score]) < 9:
                            student.used = True
                            count += 1
                            roles[score].append(student)
        highest_score -= 1
        if highest_score < 3:
            print(count)
            searching = False

    # TODO: Return roles and remove this print struct
    for role in roles:
        print(">>", role, len(roles[role]))
        for student in roles[role]:
            print(student.name)
        print("-"*5)
