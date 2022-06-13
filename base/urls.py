from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('project/<uuid:pk>', views.project_page, name='project_page'),
    path('add-project/', views.add_project, name='add_project'),
]
