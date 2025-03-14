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


class Appointments(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"