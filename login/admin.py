from django.contrib import admin
from .models import Employee,otp_handler
# Register your models here.

class AdminEmp(admin.ModelAdmin):
    list_display = ['EmployeeID','EmployeeName']

class AdminOtp(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Employee,AdminEmp)

admin.site.register(otp_handler,AdminOtp)