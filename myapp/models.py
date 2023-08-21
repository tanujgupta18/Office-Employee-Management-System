from django.db import models
from datetime import date
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50,null=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.name

class Emp(models.Model):
    fname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    # hire_date = models.DateField(("Date"), default=date.today)

    def __str__(self):
        return "%s %s %s" %(self.fname,self.lname,self.phone)