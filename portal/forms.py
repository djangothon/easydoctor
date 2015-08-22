from django.forms import ModelForm
from .models import doctor, patient
from django.core.exceptions import NON_FIELD_ERRORS

class doctorForm(ModelForm):
    class Meta:
		model = doctor
		fields = ['firstName', 'lastName', 'emailId', 'password', 'speciality']

class patientForm(ModelForm):
	class Meta:
		model = patient
		fields = ['firstName', 'lastName', 'emailId', 'password']