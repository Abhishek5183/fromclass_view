from django.db import models

# Create your models here.
class Student(models.Model):
    st_name = models.CharField(max_length=100)
    st_age = models.IntegerField()

    def __str__(self) -> str:
        return self.st_name