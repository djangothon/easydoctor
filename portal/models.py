from django.db import models

class doctor(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    emailId = models.EmailField(max_length=30, unique=True)
    speciality = models.CharField(max_length=30)
    patients = models.CharField(max_length=30)

class patient(models.Model):
	firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    emailId = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    illness = models.CharField(max_length=30)

class illness(models.Model):
	patientEmail = models.EmailField(max_length=30)
	doctorEmail = models.EmailField(max_length=30)



