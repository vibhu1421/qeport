from django.db import models
from django.utils import timezone


class RallyDefects(models.Model):
    defectid = models.CharField(max_length=200)
    description = models.TextField()
    owner=  models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    

    def __str__(self):
        return self.defectid

# Create your models here.
