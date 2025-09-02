
from django.forms import ModelForm

from roadapp.models import *


class AuthorityForm(ModelForm):
    class Meta:
        model = AuthorityTable
        fields = ['Name','Email','Phone','Department','Place','Address']

class AssignWorkForm(ModelForm):
    class Meta:
        model = AssignWorkTable
        fields = ['AUTHORITY_ID','USERID','REPORT_ID','Enddate','Status']

class IssueForm(ModelForm):
    class Meta:
        model = IssueTable
        fields = ['USERID','AUTHORITY_ID','ASSIGN_WORK','Issue','Description','Comment']

class ComplaintForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['USERID','Incident','Description','Status']       

class ReplyForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Reply']
