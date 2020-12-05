from django.db import models
# Create your models here.

class registeration(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField()
    img = models.ImageField(upload_to = 'FaceImages', verbose_name="Profile Picture")
    email = models.EmailField()
    department = models.CharField(max_length=4)
        
    def __str__(self):
        return self.name