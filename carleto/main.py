# -*- coding: utf-8 -*-

from carleto.student.student import TemplateStudent, Competence

facilitador = TemplateStudent("facilitador", {Competence.ORGANIZATION, Competence.EMPATHY, Competence.COMMUNICATION})
facilitador.set_competences(3, 5, 4, 1, 2)

pesquisador = TemplateStudent("pesquisador", {Competence.CURIOSITY, Competence.ORGANIZATION, Competence.COMMUNICATION})
pesquisador.set_competences(3, 4, 1, 5, 2)

analista = TemplateStudent("analista", {Competence.INTERPRETATION, Competence.COMMUNICATION, Competence.ORGANIZATION})
analista.set_competences(4, 3, 1, 2, 5)

revisor = TemplateStudent("revisor", {Competence.CURIOSITY, Competence.INTERPRETATION, Competence.COMMUNICATION})
revisor.set_competences(3, 1, 2, 5, 4)

suporte = TemplateStudent("suporte", {Competence.COMMUNICATION, Competence.EMPATHY, Competence.INTERPRETATION})
suporte.set_competences(5, 2, 4, 1, 3)
