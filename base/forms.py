from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class': 'form__input'})

    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'body', 'tags']
