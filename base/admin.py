from .models import Tag, Project, Skill
from django.contrib import admin

# class ProjectTagInLine(admin.TabularInline):
#     model = Tag

# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title')

admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Project)
