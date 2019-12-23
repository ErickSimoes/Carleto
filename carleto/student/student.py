from enum import Enum


class Competence(Enum):
    COMMUNICATION = 1
    ORGANIZATION = 2
    EMPATHY = 3
    CURIOSITY = 4
    INTERPRETATION = 5


class Student:
    def __init__(self, communication, organization, empathy, curiosity, interpretation):
        self.competences = dict()
        self.competences[Competence.COMMUNICATION] = communication
        self.competences[Competence.ORGANIZATION] = organization
        self.competences[Competence.EMPATHY] = empathy
        self.competences[Competence.CURIOSITY] = curiosity
        self.competences[Competence.INTERPRETATION] = interpretation


class TemplateStudent(Student):
    def __init__(self, communication, organization, empathy, curiosity, interpretation, preferences):
        super().__init__(communication, organization, empathy, curiosity, interpretation)
        self.preferences = preferences
