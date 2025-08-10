from django.db import models
from django.utilis import timezone

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['-publish']
    """
    We indicate descending order by using a hyphen before the field name
    We use the ordering attribute to tell Django that it should sort 
    results by the publish field.
    """
    indexes = [models.Index(fields=['-publish']),]
    
def __str__(self):
    return self.title