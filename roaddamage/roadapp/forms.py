
from django.forms import ModelForm

from roadapp.models import *


class AuthorityForm(ModelForm):
    class Meta:
        model = AuthorityTable
        fields = ['Email','Phone','Department','Place','Address']



class ComplaintForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['USERID','Incident','Description','Status']       

class ReplyForm(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Reply']

class IncidentForm(ModelForm):
    class Meta:
        model = IncidentTable
        fields = ['Incident', 'AUTHORITY_ID']
class AssignWorkForm(ModelForm):
    class Meta:
        model = AssignWorkTable
        fields = ['Enddate']         

