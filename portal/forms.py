from django.forms import ModelForm
from .models import doctor 
from django.core.exceptions import NON_FIELD_ERRORS

class doctorForm(ModelForm):
    class Meta:
		model = doctor
		fields = ['firstName', 'lastName', 'emailId', 'password']

class patientForm(ModelForm):
	class Meta:
		model = doctor
		fields = ['firstName', 'lastName', 'emailId', 'password']