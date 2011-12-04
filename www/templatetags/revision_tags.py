from django import template
from www import models
from git import *
import os

register = template.Library()


@register.inclusion_tag('revisions.html')
def display_revisions(requisite_id):
    print 'ok' + str(requisite_id)
    requisite = models.Requisite.objects.get(id=requisite_id)
    repoPath = os.path.dirname(requisite.project.repositoryPath + "/")
    repo = Repo(repoPath)
    g = repo.git
    fileName = 'requisites/' + requisite.requisiteType.acronym + '%03d' % requisite.number + '.md'
    log = g.log(fileName, pretty="format: '%H;%s;%an;%ar")
    log = log[1:].replace('ago', 'atras').replace('second', 'segundo').replace('minute', 'minuto').replace('hour', 'hora').replace('day', 'dia').replace('week', 'semana').replace('months', 'meses').replace('month', 'mes').replace("'", "")
    log = log.split('\n ')
    tab = []
    for l in log:
        l = l.split(';')
        tab.append(dict(changeset=l[0], description=l[1], author=l[2], life=l[3], requisite=requisite.id))
    return {'revisions': tab}


 