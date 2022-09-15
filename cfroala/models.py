from django.db import models
from froala_editor.fields import FroalaField
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    short_detail = models.TextField(blank=True, null=True)
    content = FroalaField(blank=True, null=True)

class TinyPost(models.Model):
    title = models.CharField(max_length=50)
    short_detail = models.TextField(blank=True, null=True)
    content = HTMLField(blank=True, null=True)
    document = FileBrowseField("PDF", max_length=200, directory="documents/", extensions=[".pdf",".doc"], blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tpost', args=[self.pk])
