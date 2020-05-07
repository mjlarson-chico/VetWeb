from django.db import models
from markdownx.models import MarkdownxField

# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Resources(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    uri = models.URLField()
    summary = models.CharField(max_length=255)
    description = models.TextField(max_length=8000)
    descriptionMD = MarkdownxField()
    has_guides = models.BooleanField()
    has_comments = models.BooleanField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('myapp.views.resource', args=[self.category, self.title])


class Guides(models.Model):
    title = models.CharField(max_length=50)
    body = MarkdownxField()
    resource = models.ForeignKey(Resources, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title
