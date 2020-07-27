from django.db import models
from django.utils import  timezone

class Card(models.Model):

    #title and center info
    title = models.CharField(max_length=200)
    eudra_number = models.CharField(max_length=14)
    cebk_number = models.CharField(max_length=14)
    sponsor = models.TextField()
    center_number = models.CharField(max_length=6)
    center_name = models.TextField()
    crf_version = models.CharField(max_length=20)

    #doctor's name
    doctor_name = models.CharField(max_length=25)
    doctor_phonenumber = models.CharField(max_length=15)
    doctor_fax = models.CharField(max_length=20)
    doctor_email = models.CharField(max_length=20)

    #patient
    patient_initials = models.CharField(max_length=2)
    scrining_number = models.CharField(max_length=5) #osobno numery?

    def __str__(self):
        return self.title