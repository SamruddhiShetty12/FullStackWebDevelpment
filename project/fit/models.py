from django.db import models
from django.contrib.auth.models import User 
class fit(models.Model):
    Firstname=models.CharField(max_length=50)
    Secondname=models.CharField(max_length=50)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__ (self):
        return f"{self.Firstname}{self.Secondname}-{self.Email}"

