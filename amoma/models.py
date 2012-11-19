from django.db import models
import datetime
from django.utils import dateformat
from django import forms

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
)

MARITAL_STATUS_CHOICES = (
	('S', 'Single'),
	('M', 'Married'),
	('W', 'Widow'),
	('D', 'Divorced'),
 )

class Person(models.Model):
 firstname = models.CharField(max_length=200)
 middlename = models.CharField(max_length=200)
 lastname = models.CharField(max_length=200)
 address = models.CharField(max_length=200)
 age = models.IntegerField()
 telNo = models.CharField(max_length=200)
 gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
 marital = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
 citizenship = models.CharField(max_length=200)
 religion = models.CharField(max_length=200)
 birthdate = models.DateField(max_length=15)

 #def get_consultation_date(self):
  #return dateformat.format(self.consultation_date, 'F j, Y')

class Patient(Person):
 registration_date	= models.DateField(max_length=15, default=datetime.date.today)
 notes	= models.TextField(blank=True)

 def __unicode__(self):
	return "%s %s %s" % (self.firstname, self.middlename, self.lastname)

class CustomModelChoiceField(forms.ModelChoiceField):
 def label_from_instance(self, obj):
  return "%s %s %s" % (obj.firstname, obj.middlename, obj.lastname)

class PatientRecord(models.Model):
 patient = models.ForeignKey('Patient')
 consultation_date = models.DateField(default=datetime.date.today)
 diagnosis = models.TextField(blank=True)
 labresults = models.TextField(blank=True)
 prescription = models.TextField(blank=True)

class PatientRecordForm(forms.ModelForm):
 patient = CustomModelChoiceField(queryset=Patient.objects.all())
 class Meta:
	model = PatientRecord
