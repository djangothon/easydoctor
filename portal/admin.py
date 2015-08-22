from django.contrib import admin

# Register your models here.

from portal.models import doctor, patient

admin.site.register(doctor)
admin.site.register(patient)
