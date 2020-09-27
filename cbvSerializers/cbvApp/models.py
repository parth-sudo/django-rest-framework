from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80,default='Course')
    score = models.DecimalField(max_digits=2,decimal_places=1)

    def __str__(self):
        return self.name
