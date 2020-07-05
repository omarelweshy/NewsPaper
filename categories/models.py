from django.db import models
from autoslug import AutoSlugField
from author.decorators import with_author

class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)
    def __str__(self):
        return self.name
