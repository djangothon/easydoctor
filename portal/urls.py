from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^doctorDashboard/', views.doctorDashboard, name='doctorDashboard'),
    url(r'^patientDashboard/', views.patientDashboard, name='patientDashboard'),
    url(r'^register/', views.register, name='register'),
    url(r'^showDoctor/(?P<doctorId>[0-9]+)/$', views.showDoctor, name='showDoctor'),
]