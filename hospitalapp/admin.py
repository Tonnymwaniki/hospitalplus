from django.contrib import admin
from hospitalapp.models import *

# Register your models here.
admin.site.register(patient)
admin.site.register(Doctor)
admin.site.register(staff)
admin.site.register(ward)
admin.site.register(Appointments)
admin.site.register(Contact)