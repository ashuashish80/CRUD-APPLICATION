from django.db import models

# Create your models here.
class m_create(models.Model):
    name = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 10)
    CurrentLoactio = models.CharField(max_length = 10)
    mobilenumber = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
    