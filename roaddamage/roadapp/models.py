from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=20,null=True,blank=True)
    Password=models.CharField(max_length=20,null=True,blank=True)
    UserType=models.CharField(max_length=20,null=True,blank=True)

class UserTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=20,null=True,blank=True) 
    Age=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=20,null=True,blank=True)
    Address=models.CharField(max_length=50,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
class Department(models.Model):  
    deptname=models.CharField(max_length=100,null=True,blank=True) 

class AuthorityTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    Place=models.CharField(max_length=20,null=True,blank=True)
    Address=models.CharField(max_length=50,null=True,blank=True)

class AlertTable(models.Model):
    AUTHORITY_ID=models.ForeignKey(AuthorityTable,on_delete=models.CASCADE,null=True,blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)
    Time=models.DateTimeField(auto_now_add=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    Image=models.FileField(null=True,blank=True)

class ReportTable(models.Model):
    USER_ID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    DEPARTMENT_ID=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)
    Time=models.DateTimeField(auto_now_add=True)
    Date=models.DateField(auto_now_add=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    Image=models.FileField(null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True)

class IncidentTable(models.Model):
    AUTHORITY_ID=models.ForeignKey(AuthorityTable,on_delete=models.CASCADE,null=True,blank=True)
    Incident=models.CharField(max_length=200,null=True,blank=True)

class MapViewTable(models.Model):
    # Time=models.DateTimeField(null=True,blank=True)
    Date=models.DateTimeField(auto_now_add=True)
    Incident=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True,default='pending')
    Latitude=models.FloatField(max_length=50,null=True,blank=True)
    longitude=models.FloatField(max_length=50,null=True,blank=True)






class FeedBackTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Rating=models.FloatField(null=True,blank=True)
    Review=models.CharField(max_length=200,null=True,blank=True)
    Image=models.FileField(null=True,blank=True)
    Date=models.DateField(auto_now_add=True)


class ComplaintTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Incident=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True)
    Reply=models.CharField(max_length=20,null=True,blank=True, default='pending')
    Date=models.DateField(auto_now_add=True)


class AssignWorkTable(models.Model):
   
    REPORT_ID=models.ForeignKey(ReportTable,on_delete=models.CASCADE,null=True,blank=True,related_name='assignments')

    Enddate=models.DateField(null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True,default='pending')



