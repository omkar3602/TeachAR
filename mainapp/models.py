from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tagline = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='subjects/')

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    link = models.CharField(max_length=50)
    qr_code = models.ImageField(upload_to ='topics/qr_codes/')
    image = models.ImageField(upload_to ='topics/')

    def __str__(self):
        return self.name