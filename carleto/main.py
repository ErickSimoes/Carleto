# -*- coding: utf-8 -*-

from carleto.student.student import TemplateStudent, Competence

facilitator = TemplateStudent("facilitator", {Competence.ORGANIZATION, Competence.EMPATHY, Competence.COMMUNICATION})
facilitator.set_competences(3, 5, 4, 1, 2)

researcher = TemplateStudent("researcher", {Competence.CURIOSITY, Competence.ORGANIZATION, Competence.COMMUNICATION})
researcher.set_competences(3, 4, 1, 5, 2)

analyst = TemplateStudent("analyst", {Competence.INTERPRETATION, Competence.COMMUNICATION, Competence.ORGANIZATION})
analyst.set_competences(4, 3, 1, 2, 5)

reviser = TemplateStudent("reviser", {Competence.CURIOSITY, Competence.INTERPRETATION, Competence.COMMUNICATION})
reviser.set_competences(3, 1, 2, 5, 4)

support = TemplateStudent("support", {Competence.COMMUNICATION, Competence.EMPATHY, Competence.INTERPRETATION})
support.set_competences(5, 2, 4, 1, 3)
