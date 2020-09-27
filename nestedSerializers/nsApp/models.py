from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    author = models.ForeignKey(Author,
                               related_name='books',
                               on_delete=models.CASCADE)
