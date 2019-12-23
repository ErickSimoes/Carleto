# -*- coding: utf-8 -*-

from enum import Enum


class Competence(Enum):
    COMMUNICATION = 1
    ORGANIZATION = 2
    EMPATHY = 3
    CURIOSITY = 4
    INTERPRETATION = 5


class Student:
    def __init__(self, name):
        self.name = name
        self.competences = dict()

    def set_competences(self, communication, organization, empathy, curiosity, interpretation):
        self.competences[Competence.COMMUNICATION] = communication
        self.competences[Competence.ORGANIZATION] = organization
        self.competences[Competence.EMPATHY] = empathy
        self.competences[Competence.CURIOSITY] = curiosity
        self.competences[Competence.INTERPRETATION] = interpretation


class TemplateStudent(Student):
    def __init__(self, communication, organization, empathy, curiosity, interpretation, preferences):
        super().__init__(communication, organization, empathy, curiosity, interpretation)
        self.preferences = preferences
