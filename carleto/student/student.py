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

    def set_competences(self, communication: int, organization: int, empathy: int, curiosity: int, interpretation: int):
        self.competences[Competence.COMMUNICATION] = int(communication)
        self.competences[Competence.ORGANIZATION] = int(organization)
        self.competences[Competence.EMPATHY] = int(empathy)
        self.competences[Competence.CURIOSITY] = int(curiosity)
        self.competences[Competence.INTERPRETATION] = int(interpretation)

    def set_class(self, room_class: str):
        self.room_class = room_class


# TODO: Dismiss the use of a preference list. Instead, use the 3 highest value attributes
class TemplateStudent(Student):
    def __init__(self, name: str, role: Role, preferences: list):
        super().__init__(name)
        self.role = role
        self.preferences = preferences
