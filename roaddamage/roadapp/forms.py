
from django.forms import ModelForm

from roadapp.models import *


class AuthorityForm(ModelForm):
    class Meta:
        model = AuthorityTable
        fields = ['Department','Email','Phone','Department','Place','Address']



class ComplaintForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['USERID','Incident','Description','Status']       

class ReplyForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Reply']


class AssignWorkForm(ModelForm):
    class Meta:
        model = AssignWorkTable
        fields = ['Enddate']         

class departmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['deptname']         
