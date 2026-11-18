from django.db import models

class StudentData(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField()
    dept = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
