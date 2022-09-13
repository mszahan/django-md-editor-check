from django.db import models
from froala_editor.fields import FroalaField



class Post(models.Model):
    title = models.CharField(max_length=50)
    short_detail = models.TextField(blank=True, null=True)
    content = FroalaField(blank=True, null=True)
