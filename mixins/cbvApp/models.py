from django.db import models

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2,decimal_places=1)

    def __str__(self):
        return self.name


