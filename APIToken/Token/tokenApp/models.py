from django.db import models
# Create your models here.
class UserList(models.Model):

    username = models.CharField(max_length=233)
    firstname = models.CharField(max_length=233)

    def __str__(self):

        return self.firstname
