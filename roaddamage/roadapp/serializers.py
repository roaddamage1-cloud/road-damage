from rest_framework.serializers import ModelSerializer
from roadapp.models import *

class Authorityserializer(ModelSerializer):
    class Meta:
        model = AuthorityTable
        fields = ['Email','Phone','Department','Place','Address']

class Loginserializer(ModelSerializer):
    class Meta:
        model=LoginTable
        fields=['Username','Password','UserType']

class Userserializer(ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['LOGIN','Name','Age','Email','Gender','Address','Phone','Place']


class Alertserializer(ModelSerializer):
    class Meta:
        model = AlertTable
        fields = ['Time','location','message','image']


class Reportserializer(ModelSerializer):
    class Meta:
        model = ReportTable
        fields = ['Message','Time','date','location','Image','Description','status'] 

class Incidentserializer(ModelSerializer):
    class Meta:
        model = IncidentTable
        fields = ['Incident'] 
class Mapviewserializer(ModelSerializer):
    class Meta:
        model = MapViewTable
        fields = ['date','location','incident','status'] 
class FeedBackserializer(ModelSerializer):
    class Meta:
        model = FeedBackTable
        fields = ['Rating','Review','Image','Date'] 

class Complaintserializer(ModelSerializer):
    class Meta:
        model=ComplaintTable
        fields=['Incident','Description','Status','Reply','Date']



