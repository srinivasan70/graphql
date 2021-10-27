from django.db import models

# Create your models here.

class Userdata(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

def _str_(self):
    return self.username, self.email, self.firstname, self.lastname
    
