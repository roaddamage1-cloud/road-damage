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

class AuthorityTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=20,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Phone=models.BigIntegerField(null=True,blank=True)
    Department=models.CharField(max_length=20,null=True,blank=True)
    Place=models.CharField(max_length=20,null=True,blank=True)
    Address=models.CharField(max_length=50,null=True,blank=True)

class AlertTable(models.Model):
    AUTHORITY_ID=models.ForeignKey(AuthorityTable,on_delete=models.CASCADE,null=True,blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)
    Time=models.DateTimeField(auto_now_add=True)
    Location=models.CharField(max_length=50,null=True,blank=True)

class ReportTable(models.Model):
    AUTHORITY_ID=models.ForeignKey(AuthorityTable,on_delete=models.CASCADE,null=True,blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)
    Time=models.DateTimeField(auto_now_add=True)
    Date=models.DateField(auto_now_add=True)
    Location=models.CharField(max_length=50,null=True,blank=True)
    Image=models.FileField(null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True)

class MapViewTable(models.Model):
    Time=models.DateTimeField(null=True,blank=True)
    Date=models.DateField(auto_now_add=True)
    Incident=models.CharField(max_length=200,null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True)
    Location=models.CharField(max_length=50,null=True,blank=True)

class ContactTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    Contactnumber=models.BigIntegerField(null=True,blank=True)
    Department=models.CharField(max_length=20,null=True,blank=True)
    Place=models.CharField(max_length=50,null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)

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
    Reply=models.CharField(max_length=20,null=True,blank=True)
    Date=models.DateField(auto_now_add=True)


class AssignWorkTable(models.Model):
    AUTHORITY_ID=models.ForeignKey(AuthorityTable,on_delete=models.CASCADE,null=True,blank=True)
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    REPORT_ID=models.ForeignKey(ReportTable,on_delete=models.CASCADE,null=True,blank=True)
    Startdate=models.DateField(auto_now_add=True)
    Enddate=models.DateField(null=True,blank=True)
    Status=models.CharField(max_length=20,null=True,blank=True)

class IssueTable(models.Model):
    USERID=models.ForeignKey(UserTable,on_delete=models.CASCADE,null=True,blank=True)
    AUTHORITY_ID=models.ForeignKey(AuthorityTable,on_delete=models.CASCADE,null=True,blank=True)
    ASSIGN_WORK=models.ForeignKey(AssignWorkTable,on_delete=models.CASCADE,null=True,blank=True)
    Issue=models.CharField(max_length=50,null=True,blank=True)
    Description=models.CharField(max_length=200,null=True,blank=True)
    Date=models.DateField(auto_now_add=True)
    Comment=models.CharField(max_length=200,null=True,blank=True)


