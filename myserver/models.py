from django.db import models

class Status(models.Model):
    describe = models.CharField(max_length=100)

    def __str__(self):
        return self.describe

class Pattern(models.Model):
    describe = models.CharField(max_length=100)
    def __str__(self):
        return self.describe


# Create your models here.
class Server(models.Model):
    host_name = models.CharField(max_length=100)
    describe = models.TextField()
    intranet_ip = models.CharField(max_length=100)
    internet_ip = models.CharField(max_length=100, blank=True)
    domain = models.BooleanField()
    os = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey('Status')
    pattern = models.ForeignKey('Pattern')
    local_account = models.CharField(max_length=100)
    local_password = models.CharField(max_length=100)
    manage_account = models.CharField(max_length=100, blank=True)
    manage_password = models.CharField(max_length=100, blank=True)
    postion = models.CharField(max_length=100)

    def __str__(self):
        return self.host_name


class Service(models.Model):
    server = models.ForeignKey('Server')
    describe = models.CharField(max_length=100)
    manage_method = models.CharField(max_length=100)
    manage_account = models.CharField(max_length=100)
    manage_password = models.CharField(max_length=100)
