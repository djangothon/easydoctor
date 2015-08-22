from django.forms import ModelForm
from .models import doctor, patient, profile, diagnosis, appointment, onlineConsultation, allergie
from django.core.exceptions import NON_FIELD_ERRORS

class doctorForm(ModelForm):
    class Meta:
		model = doctor
		fields = ['firstName', 'lastName', 'emailId', 'password', 'speciality']

class patientForm(ModelForm):
	class Meta:
		model = patient
		fields = ['firstName', 'lastName', 'emailId', 'password']

class profileForm(ModelForm):
	class Meta:
		model = profile
		fields = ['gender','age','phone','address']

class diagnosisForm(ModelForm):
	class Meta:
		model = diagnosis
		fields = ['ailment','doctorName','doctorEmail']


class appointmentForm(ModelForm):
	class Meta:
		model = appointment
		fields = ['last','next']

class consultationForm(ModelForm):
	class Meta:
		model = onlineConsultation
		fields = ['last','next']

class allergies(ModelForm):
	class Meta:
		model = allergie
		fields = ['email','allergies']
