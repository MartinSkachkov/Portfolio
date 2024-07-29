from django.db import models

# Create your models here.
class Project(models.Model):
     name = models.CharField(max_length=200)
     category = models.CharField(max_length=100)
     github_link = models.URLField(blank=True, null=True)
     video_link = models.URLField(blank=True, null=True)
     description = models.TextField()

     def __str__(self):
        return self.name