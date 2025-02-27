from django.db import models

# Create your models here.

class patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class staff(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    position = models.CharField(max_length=60)
    phenomenal = models.CharField(max_length=50)
    email = models.EmailField()
    hiredate = models.DateField()

    def __str__(self):
        return self.firstname

class ward(models.Model):
    name = models.CharField(max_length=50)
    totalbeds = models.CharField(max_length=50)
    availablebeds = models.CharField(max_length=50)

    def __str__(self):
        return self.name
