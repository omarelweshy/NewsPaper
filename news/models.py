import uuid
from django.db import models
# from autoslug import AutoSlugField
from author.decorators import with_author
from categories.models import *
from django.urls import reverse

@with_author
class Report(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,
                        editable=False)
    category = models.ForeignKey(Categories, 
        on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='news_images')
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("report_detail", kwargs={"pk": self.pk})
    
# @with_author
# class Headline(models.Model):
#     title = models.CharField(max_length=50)
#     slug = AutoSlugField(populate_from='title', unique=True)
#     body = models.TextField()
#     image = models.ImageField(upload_to='news_images')
#     date = models.DateTimeField(auto_now=True)