from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE =[
        ('admin','اداري'),
        ('teacher','استاذ'), 
        ('student', 'طالب'),
        ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    phone_number = models.CharField(max_length=11, null=True , blank=True )


    def __str__(self):
        return str(self.user)

