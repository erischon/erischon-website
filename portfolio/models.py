from django.db import models


class Techno(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=150)
    detail = models.TextField()
    image = models.ImageField(upload_to='blog/')
    url_project = models.CharField(max_length=250)
    url_git = models.CharField(max_length=250)
    techno = models.ManyToManyField(Techno)

    def __str__(self):
        return self.title

