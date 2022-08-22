from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator,RegexValidator

class Employee(models.Model):
    EmployeeID=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=25)
    DOB=models.DateField()
    phone_regex = RegexValidator(regex=r'\d{9,13}')
    Phone = models.CharField(validators=[phone_regex], max_length=15)
    Email=models.EmailField(max_length=30,unique=True)
    Street=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    Country=models.CharField(max_length=20)
    PINCODE=models.CharField(max_length=7)

    def __str__(self):
        id=str(self.EmployeeID)+' - '+ self.EmployeeName
        return id
class otp_handler(models.Model):
    email=models.CharField(max_length=30)
    last_otp=models.IntegerField()