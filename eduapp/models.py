from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    student_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    mobile=models.CharField(max_length=10)
    profile_img=models.ImageField(upload_to="images", blank=True,null=True)
    email=models.CharField(max_length=200)

