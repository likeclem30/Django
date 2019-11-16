from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=600)
    web_link = models.CharField(max_length=600,null=True, blank=True)
    video_link = models.CharField(max_length=600,null=True, blank=True)
    image = models.ImageField(upload_to="images/")
