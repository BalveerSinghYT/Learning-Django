from django.contrib import admin
from .models import registeration

# Register your models here.
admin.site.register(registeration)

admin.site.site_title = "Face Recognition Attendance System"
admin.site.site_header = "Facial Recognition Admin Login"
