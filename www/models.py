# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import  models
from sys import *

ROLES = (('Mg', 'Gerente'),
        ('An', 'Analista'),
        ('Us', 'Usuario'))

URGENCY_LEVEL = ((1, 'Muito Urgente'),
                (2, 'Urgente'),
                (3, 'Normal'),
                (4, 'Não é urgente'))


class Project(models.Model):
    name = models.CharField(max_length=60)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __unicode__(self):
        return self.name


class ProjectMember(models.Model):
    user = models.ForeignKey(User, unique=True, verbose_name=('user'))
    project = models.ForeignKey(Project)
    role = models.CharField(max_length=2, choices=ROLES)

    def __unicode__(self):
        return self.user.username


class RequisiteType(models.Model):
    acronym = models.CharField(max_length=10, blank=False)
    description = models.CharField(max_length=50, blank=False)

    def __unicode__(self):
        return self.description


class Requisite(models.Model):
    project = models.ForeignKey(Project)
    requisiteType = models.ForeignKey(RequisiteType)
    title = models.CharField(max_length=100)
    description = models.TextField()
    urgency = models.SmallIntegerField(default=3, choices=URGENCY_LEVEL)

    def __unicode__(self):
        return self.title

