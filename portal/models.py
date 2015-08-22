from django.db import models

class doctor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    emailId = models.EmailField(max_length=30, unique=True)
    speciality = models.CharField(max_length=30)
    patients = models.CharField(max_length=30)

    def __unicode__(self):
        return self.firstName

class patient(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    emailId = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    illness = models.CharField(max_length=30)

    def __unicode__(self):
        return self.firstName

class profile(models.Model):
    gender = models.IntegerField(max_length=10)
    age = models.CharField(max_length=3)
    phone = models.IntegerField(max_length=15)
    address = models.TextField(max_length=60)

class diagnosis(models.Model):
    ailment = models.CharField(max_length=30)
    doctorName = models.CharField(max_length=30)
    doctorEmail = models.CharField(max_length=30)

class appointment(models.Model):
    last = models.DateField(max_length=30)
    next = models.DateField(max_length=30)

class onlineConsultation(models.Model):
    last = models.DateField(max_length=30)
    next = models.DateField(max_length=30)

class allergie(models.Model):
    email = models.EmailField(max_length=30, unique=True)
    allergies = models.TextField(max_length=30)



