from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Student(AbstractUser):
    course=models.CharField(max_length=25)
    date_of_birth=models.DateField(max_length=25)
    profile_image=models.ImageField(upload_to='profile_pics/',null=True,blank=True)