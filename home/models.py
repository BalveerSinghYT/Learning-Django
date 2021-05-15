from django.db import models
from django.core.validators import RegexValidator
import os

from django.db.models.fields.related import ForeignKey
# Create your models here.

def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    print(basefilename)
    return 'FaceImages/{basename}{ext}'.format(basename= instance.name, ext= file_extension)

class registeration(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=6, validators=[RegexValidator(r'^\d{1,10}$')])
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to = photo_path, verbose_name="Profile Picture")
    email = models.EmailField()
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{0,10}$')])
    department = models.CharField(max_length=4)
        
    def __str__(self):
        return self.name

class attendance(models.Model):
    roll_no = models.OneToOneField(registeration, on_delete=models.CASCADE, primary_key=True)
    date = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=7)
