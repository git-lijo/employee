from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class EmployeeData(models.Model):
    EmpId = models.AutoField(primary_key=True)
    EmpName = models.CharField(max_length=50)
    EmpMail = models.EmailField(max_length=255)
    Password = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=12)
    Address = models.TextField()

    def __str__(self):
        return self.EmpName

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
