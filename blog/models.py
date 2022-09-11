from django.db import models

class Blog(models.Model): # inherits from model class 

    title = models.CharField(max_length=200)
    date = models.DateField()
    message = models.TextField()
    
