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