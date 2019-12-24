# -*- coding: utf-8 -*-

from enum import Enum


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

    def set_competences(self, communication: int, organization: int, empathy: int, curiosity: int, interpretation: int):
        self.competences[Competence.COMMUNICATION] = communication
        self.competences[Competence.ORGANIZATION] = organization
        self.competences[Competence.EMPATHY] = empathy
        self.competences[Competence.CURIOSITY] = curiosity
        self.competences[Competence.INTERPRETATION] = interpretation

    def set_class(self, room_class: str):
        self.room_class = room_class


class TemplateStudent(Student):
    def __init__(self, name: str, preferences: list):
        super().__init__(name)
        self.preferences = preferences
