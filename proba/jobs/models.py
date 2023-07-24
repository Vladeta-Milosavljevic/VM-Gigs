from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Job(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='job_logo/', null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    custom_tags = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=128)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    
