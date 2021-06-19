from django.db import models
from uuid import uuid4

class Student(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    dob = models.DateField()

    def __str__(self):
        return self.firstname