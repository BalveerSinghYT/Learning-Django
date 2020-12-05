from django.db import models
import os
# Create your models here.

def photo_path(instance, filename):
    basefilename, file_extension= os.path.splitext(filename)
    print(basefilename)
    return 'FaceImages/{basename}{ext}'.format(basename= instance.name, ext= file_extension)

class registeration(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField()
    img = models.ImageField(upload_to = photo_path, verbose_name="Profile Picture"    )
    email = models.EmailField()
    department = models.CharField(max_length=4)
        
    def __str__(self):
        return self.name

