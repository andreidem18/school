from students.models import Student
from django.db import models
from uuid import uuid4

class Class(models.Model):
    name = models.CharField(max_length=150)
    credits = models.IntegerField()
    student = models.ManyToManyField(
        Student,
        related_name='classes'
    )

    def __str__(self):
        return self.name