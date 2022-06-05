from django.db import models
import uuid

from config.settings import MEDIA_ROOT


class UUIDgenerateMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Tag(UUIDgenerateMixin, models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(UUIDgenerateMixin, models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(UUIDgenerateMixin, models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, upload_to='projects_logo')
    body = models.TextField(null=True)
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(to=Tag, related_name='projects')

    def __str__(self):
        return self.title
