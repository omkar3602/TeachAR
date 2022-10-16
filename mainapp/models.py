from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='subjects/')

    def __str__(self):
        return self.name