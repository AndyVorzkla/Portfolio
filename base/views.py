import uuid

from django.db.models import Q
from django.shortcuts import render

from base.models import Project, Skill


def home_page(request):
    projects = Project.objects.all()
    detail_skills = Skill.objects.filter(~Q(body=''))
    skills = Skill.objects.filter(body='')

    context = {
        'projects': projects,
        'detail_skills': detail_skills,
        'skills': skills,
    }

    return render(request, 'base/home.html', context=context)


def project_page(request, pk: uuid):
    try:
        project = Project.objects.get(id=pk)
    except Project.DoesNotExist:
        project = None

    context = {
        'project': project,
    }
    return render(request, 'base/project.html', context=context)


def create_project(request):
    context = {}
    return render(request, 'base/project_form.html', context=context)
