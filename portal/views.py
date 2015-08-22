from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from portal.forms import doctorForm, patientForm
from portal.models import doctor, patient 


def index(request) :
	return render(request, 'easydoctor/index.html')


def doctorDashboard(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		return render(request, 'easydoctor/doctorDashboard.html')

def patientDashboard(request):
	if 'session_id' not in request.session:
		return redirect('http://localhost:8000/portal/')
	else:
		return render(request, 'easydoctor/patientDashboard.html')

def register (request):
	
	category = request.POST['category']
	if category == 'Doctor':
		data = doctorForm(request.POST)
		if data.is_valid():
	  		data.save()
			return(HttpResponse('<p>Thank you</p>'))
		else :
			return(HttpResponse('<p>Could not Register</p>'))
	else :
		data = patientForm(request.POST)
		print data
		if data.is_valid():
	  		data.save()
			return(HttpResponse('<p>Thank you</p>'))
		else :
			return(HttpResponse('<p>Could not Register</p>'))

def showDoctor (request, doctorId):
	e = doctor.objects.filter(id=doctorId)
	doctorData = "{0}</br> {1}</br> {2}</br> {3}".format(e.first().firstName, e.first().lastName, e.first().displayName, e.first().emailId)    
	return(HttpResponse("%s" %doctorData))

def verify (request):
	email = request.POST['emailId']
	password = request.POST['password']
	category = request.POST['category']
	if category == 'doctor':
		e = doctor.objects.filter(emailId=email,password=password)
	else :
		e = patient.objects.filter(emailId=email,password=password)
		
	if e.count() == 1:

		request.session['session_id'] = request.COOKIES.get('sessionid') 
		request.session['firstName'] = e.first().firstName
		return redirect('http://localhost:8000/portal/'+ category +'Dashboard/')
	else :
		return HttpResponse("Check Credintials")

def logout(request):
    try:
        del request.session['session_id'], request.session['displayName']
    except KeyError:
        pass
    return redirect('http://localhost:8000/portal/')
    # return HttpResponse("You're logged out.")
