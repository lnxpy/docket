from django.db import models
from ckeditor.fields import RichTextField


class Documentation(models.Model):
    content = RichTextField()
    version = models.CharField(max_length=10, default='v')

    def __str__(self):
        return self.version
