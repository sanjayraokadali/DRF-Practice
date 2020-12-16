from django.db import models

# Create your models here.

class AddBook(models.Model):

    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateField()

    def __str__(self):

        return self.bookname
