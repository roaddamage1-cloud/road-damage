from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from roadapp.models import *
from roadapp.forms import *


 # /////////////////////////////////////// Administration //////////////////////////////


# Create your views here.
class login(View):
    def get(self, request):
        return render(request, "Administration/login.html")
    def post(self, request):
        username1 = request.POST['Username']
        password1 = request.POST['Password']
        try:
            obj = LoginTable.objects.get(Username=username1, Password=password1)
            request.session['username'] = obj.id

            # Handle based on user type
            if obj.UserType =='admin':
                return HttpResponse('''<script>alert("welcome back");window.location='/AdminHome'</script>''')
            elif obj.UserType =='authority':
                return HttpResponse('''<script>alert("welcome back");window.location='/AuthorityHome'</script>''')

            else:
                return HttpResponse('''<script>alert("user not found");window.location='/'</script>''')
        except LoginTable.DoesNotExist:
            #Handle care where login details does not exist
            return  HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')


class update(View):
    def get(self, request,id):
        c=ComplaintTable.objects.get(id=id)
        return render(request, "Administration/update.html",{'a':c})
    
class report(View):
    def get(self, request):
        obj = ReportTable.objects.all()
        return render(request, "Administration/report.html", {'val': obj})
    
class manageuser(View):
    def get(self, request):
        obj = UserTable.objects.all()
        return render(request, "Administration/manageuser.html", {'val': obj})
    
class manageauthority(View):
    def get(self, request):
        obj = AuthorityTable.objects.all()
        return render(request, "Administration/manageauthority.html", {'val': obj})
    
class issues(View):
    def get(self, request):
        obj = IssueTable.objects.all()
        return render(request, "Administration/issues.html", {'val': obj})
    
class feedback(View):
    def get(self, request):
        obj = FeedBackTable.objects.all()
        return render(request, "Administration/feedback.html", {'val': obj})
    
class detection(View):
    def get(self, request):
        obj = MapViewTable.objects.all()
        return render(request, "Administration/detection.html", {'val': obj})
    
class complaint(View):
    def get(self, request):
        obj = ComplaintTable.objects.all()
        return render(request, "Administration/complaint.html", {'val': obj})
    
class assignwork(View):
    def get(self, request):
        obj = AssignWorkTable.objects.all()
        return render(request, "Administration/assignwork.html", {'val': obj})
    # def post(self, request):
    #     h=
    
class addauthority(View):
    def get(self, request):
        return render(request, "Administration/addauthority.html") 
    def post(self, request):
        form= AuthorityForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN = LoginTable.objects.create(Username=request.POST['Username'], Password=request.POST['Password'], UserType="Authority")
            f.save()
            return redirect('manageauthority')
        
class AdminHome(View):
    def get(self, request):
        return render(request, "Administration/AdminHome.html")
    
 # /////////////////////////////////////   Authority    //////////////////////////////////////
    
class alert(View):
    def get(self, request):
        obj = AlertTable.objects.all()
        return render(request, "Authority/alert.html", {'val': obj} )   
    
class fdback(View):
    def get(self, request):
        obj = FeedBackTable.objects.all()
        return render(request, "Authority/fdback.html", {'val': obj})   
    
class authorityreport(View):
    def get(self, request):
        obj = ReportTable.objects.all()
        return render(request, "Authority/authorityreport.html", {'val': obj})  
     
class sendissues(View):
    def get(self, request):
        return render(request, "Authority/sendissues.html")  
     
class updatingstatus(View):
    def get(self, request):
        return render(request, "Authority/updatingstatus.html") 
      
class viewassign(View):
    def get(self, request):
        obj = AssignWorkTable.objects.all()
        return render(request, "Authority/viewassign.html", {'val': obj})
       
class viewissues(View):
    def get(self, request):
        obj = IssueTable.objects.all()
        return render(request, "Authority/viewissues.html", {'val': obj}) 
    

class AuthorityHome(View):
    def get(self, request):
        return render(request, "Authority/AuthorityHome.html",) 
      
