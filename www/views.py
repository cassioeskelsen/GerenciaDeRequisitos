from django.http import HttpResponse
from www.models import *
from django.db import *
from django.template import Context, loader


def showRevision(request, requisite_id, changeset):
#return render_to_response('estatisticas/index.html')
    requisite = Requisite.objects.get(id=requisite_id)
    repoPath = os.path.dirname(requisite.project.repositoryPath + "/")
    repo = Repo(repoPath)
    g = repo.git
    fileName = 'requisites/' + requisite.requisiteType.acronym + '%03d' % requisite.number + '.md'
    text = g.show(changeset + ':' + fileName)
    t = loader.get_template('showRevision.html')
    c = Context({
    'file': file,
    'changeset': changeset,
    'text': text,
    'title': requisite.title
    })
    return HttpResponse(t.render(c))
