from django.db import models
from ckeditor.fields import RichTextField

ALIGNMENT_CHOICES = [
    ('left', 'Left (e.g. English)'),
    ('right', 'Right (e.g. Persian, Arabic, Urdu, etc)'),
]

ALIGNMENT_HINT = """
You may use Persian language.
Don't forget to set the direction from the top corner of content editor.
"""

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('pe', 'Persian'),
]

class Documentation(models.Model):
    content = RichTextField()
    alignment = models.CharField(choices=ALIGNMENT_CHOICES, max_length=50, help_text=ALIGNMENT_HINT)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    version = models.CharField(max_length=50)

    def __str__(self):
        return self.version
