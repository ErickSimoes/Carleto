# -*- coding: utf-8 -*-

from enum import Enum


class Role(Enum):
    FACILITATOR = 1
    RESEARCHER = 2
    ANALYST = 3
    REVISER = 4
    SUPPORT = 5


class Competence(Enum):
    COMMUNICATION = 1
    ORGANIZATION = 2
    EMPATHY = 3
    CURIOSITY = 4
    INTERPRETATION = 5


class Student:
    def __init__(self, name: str):
        self.name = name
        self.competences = dict()
        self.room_class = ""
        # TODO: Fix typo of attribute to plural
        self.score = dict()
        self.used = False

    def set_competences(self, communication: int, organization: int, empathy: int, curiosity: int, interpretation: int):
        self.competences[Competence.COMMUNICATION] = int(communication)
        self.competences[Competence.ORGANIZATION] = int(organization)
        self.competences[Competence.EMPATHY] = int(empathy)
        self.competences[Competence.CURIOSITY] = int(curiosity)
        self.competences[Competence.INTERPRETATION] = int(interpretation)

    def set_class(self, room_class: str):
        self.room_class = room_class

    def calculate_score(self, templates):
        for template in templates:
            score = 0
            for competence in template.competences:
                if template.competences[competence] >= 3:
                    score += abs(abs(self.competences[competence] - template.competences[competence]) - 5)

            self.score[template.role] = score


class TemplateStudent(Student):
    def __init__(self, name: str, role: Role):
        super().__init__(name)
        self.role = role
