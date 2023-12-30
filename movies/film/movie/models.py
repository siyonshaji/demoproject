from django.db import models

# Create your models here.
class Movie(models.Model):
    image=models.ImageField(upload_to="books/cover",null=True,blank=True)
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    year=models.IntegerField()
