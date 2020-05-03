from django.db import models
from djongo import models
# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=100,default='SOME STRING')
    phone_number = models.CharField(max_length=10,default="")

    def __str__(self):
        return "Customer name is "+self.name+" & his/her email address is "+self.email_address
