# -*- coding: utf-8 -*-

from carleto.student.student import TemplateStudent, Competence, Role

facilitator = TemplateStudent("facilitator", Role.FACILITATOR, [Competence.ORGANIZATION, Competence.EMPATHY, Competence.COMMUNICATION])
facilitator.set_competences(3, 5, 4, 1, 2)

researcher = TemplateStudent("researcher", Role.RESEARCHER, [Competence.CURIOSITY, Competence.ORGANIZATION, Competence.COMMUNICATION])
researcher.set_competences(3, 4, 1, 5, 2)

analyst = TemplateStudent("analyst", Role.ANALYST, [Competence.INTERPRETATION, Competence.COMMUNICATION, Competence.ORGANIZATION])
analyst.set_competences(4, 3, 1, 2, 5)

reviser = TemplateStudent("reviser", Role.REVISER, [Competence.CURIOSITY, Competence.INTERPRETATION, Competence.COMMUNICATION])
reviser.set_competences(3, 1, 2, 5, 4)

support = TemplateStudent("support", Role.SUPPORT, [Competence.COMMUNICATION, Competence.EMPATHY, Competence.INTERPRETATION])
support.set_competences(5, 2, 4, 1, 3)
