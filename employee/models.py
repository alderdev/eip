from django.db import models

# Create your models here.
class Department(models.Model):
    describe = models.CharField(max_length=100)

    def __str__(self):
        return self.describe

class Jobtitle(models.Model):
    describe = models.CharField(max_length=100)
    def __str__(self):
        return self.describe


class Person(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    dutydate = models.DateField()
    department = models.ForeignKey('Department')
    jobtitle = models.ForeignKey('Jobtitle')
    ext_number = models.CharField(max_length = 6, blank=True )
    background = models.CharField(max_length=100)
    interest = models.TextField()

    #image = models.ImageField()
