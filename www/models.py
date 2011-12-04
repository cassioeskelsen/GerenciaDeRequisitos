# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models import Max
from django.db import  models
import os
import codecs
import tiraacentos
from sys import *
from git import *

ROLES = (('Mg', 'Gerente'),
        ('An', 'Analista'),
        ('Us', 'Usuario'))

LEVEL = ((1, 'Alta'),
                (2, 'Média'),
                (3, 'Baixa'))


class Project(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nome")
    startDate = models.DateTimeField(verbose_name="Data de Início")
    endDate = models.DateTimeField(blank=False,     verbose_name="Data de Conclusão")
    repositoryPath = models.CharField(max_length=100, blank=False, verbose_name="Localização do diretório de trabalho")

    def __unicode__(self):
        return self.name

    def clean(self):
        dir = os.path.dirname(self.repositoryPath + "/")
        if not os.path.exists(dir):
            os.makedirs(dir)

        repo = None
        try:
            repo = Repo(dir)
        except InvalidGitRepositoryError:
            repo = Repo.init(dir)

        pathReq = os.path.join(dir, 'requisites')
        if not os.path.exists(pathReq):
            os.makedirs(pathReq)
            file = open(pathReq + '/requisites.md', 'w+')
            file.write('Diretório de Requisitos\n')
            file.write('=======================\n')
            file.close()
            index = repo.index
            index.add([os.path.join(pathReq, file.name)])
            index.commit('Criação do repositório')
            repo.commit()

    class Meta:
        verbose_name = "Projeto"


class ProjectMember(models.Model):
    user = models.ForeignKey(User, unique=False, verbose_name=('Usuário'))
    project = models.ForeignKey(Project, verbose_name="Projeto")
    role = models.CharField(max_length=2, choices=ROLES, verbose_name="Função")

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Membro do Projeto'


class RequisiteType(models.Model):
    acronym = models.CharField(max_length=10, blank=False, verbose_name="Sigla")
    description = models.CharField(max_length=50, blank=False, verbose_name="Descrição")

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de Requisito'


class Requisite(models.Model):
    number = models.IntegerField(blank=False, verbose_name="Número")
    project = models.ForeignKey(Project, verbose_name="Projeto")
    requisiteType = models.ForeignKey(RequisiteType, verbose_name="Tipo de Requisito")
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    urgency = models.SmallIntegerField(default=2, choices=LEVEL, verbose_name="Prioridade")
    complexity = models.SmallIntegerField(default=2, choices=LEVEL, verbose_name="Complexidade")
    validated = models.BooleanField(default=False, verbose_name="Validado")

    def __unicode__(self):
        return self.title

    def __getNextRequisiteNumber__(self):
        ultimo = Requisite.objects.filter(project__id=self.project.id).filter(requisiteType__id=self.requisiteType.id).aggregate(Max('number'))
        if ultimo['number__max'] == None:
            return 1
        else:
            return ultimo['number__max'] + 1

    def clean(self):
        alteracao = False
        repo = Repo(self.project.repositoryPath + "/")
        pathReq = os.path.join(self.project.repositoryPath, 'requisites')
        next_number = 1
        if self.id == None:
            next_number = self.__getNextRequisiteNumber__()
            self.number = next_number
        else:
            next_number = self.number
        filename = pathReq + '/' + self.requisiteType.acronym + '%03d' % next_number + '.md'
        if os.path.isfile(filename):
            alteracao = True
        file = codecs.open(filename,  encoding='utf-8', mode='w')
        file.write('Projeto ' + self.project.name + '\n\n')
        file.write(self.requisiteType.description + ' ' + self.requisiteType.acronym + '%03d' % next_number + '\n\n')
        file.write(self.description)
        file.close()
        index = repo.index
        index.add([os.path.join(pathReq, file.name)])
        if alteracao:
            index.commit(tiraacentos.asciize('Alteracao do ' + self.requisiteType.description + ' ' + '%03d' % next_number))
        else:
            index.commit(tiraacentos.asciize('Criacao do ' + self.requisiteType.description + ' ' + '%03d' % next_number))
        repo.commit()

    class Admin:
        list_filter = ('project')

    class Meta:
        verbose_name = 'Requisito'


