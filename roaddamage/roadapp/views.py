from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from roadapp.models import *
from roadapp.forms import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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
            request.session['lid'] = obj.id

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
    def post(self, request,id):
        obj = ComplaintTable.objects.get(id=id)
        obj.Reply= request.POST['Reply']   
        obj.save()
        return redirect('complaint')
    
class report(View):
    def get(self, request):
        obj = ReportTable.objects.all()
        return render(request, "Administration/report.html", {'val': obj})
    
class manageuser(View):
    def get(self, request):
        obj = UserTable.objects.all()
        return render(request, "Administration/manageuser.html", {'val': obj})
    
class deleteuser(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.delete()
        return redirect('/manageuser')
    
class manageauthority(View):
    def get(self, request):
        obj = AuthorityTable.objects.all()
        return render(request, "Administration/manageauthority.html", {'val': obj})
    
class deleteauthority(View):
    def get(self, request, lid):
        obj = LoginTable.objects.get(id=lid)
        obj.delete()
        return redirect('/manageauthority')
    
class issues(View):
    def get(self, request):
        obj = ReportTable.objects.all()
        return render(request, "Administration/assignwork.html", {'val': obj})
    
class assignwork(View):
    def get(self, request, report_id):
        d = ReportTable.objects.get(id=report_id)
        return render(request, 'Administration/assignworks.html', {'report': d})

    def post(self, request, report_id):
        d = ReportTable.objects.get(id=report_id)
        form = AssignWorkForm(request.POST)
        if form.is_valid():
            assign = form.save(commit=False)
            assign.REPORT_ID = d
            assign.Status = 'Pending' 
            assign.save()
        return redirect('issues') 


   
class assignworksauthority(View):
    def get(self,request):
        return render(request,'assigndates.html')    
    
class addincident(View):
    def get(self, request):
        form = IncidentForm()
        authorities = AuthorityTable.objects.all()
        return render(request, "Administration/addincident.html", {
            'form': form,
            'authorities': authorities
        })

    def post(self, request):
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manageincident')
        authorities = AuthorityTable.objects.all()
        return render(request, "Administration/addincident.html", {
            'form': form,
            'authorities': authorities
        })

        
class manageincident(View):
    def get(self, request):
            obj = IncidentTable.objects.all()
            return render(request, "Administration/manageincident.html", {'val': obj})

class deleteIncident(View):
    def get(self, request, lid):
        obj = IncidentTable.objects.get(id=lid)
        obj.delete()
        return redirect('/manageincident')


       
    
         
    
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


class viewassignAdmin(View):
    def get(self, request):
        obj = AssignWorkTable.objects.all()
        return render(request, "Administration/viewassignAdmin.html", {'val': obj})
       


class IssueListView(View):
    def get(self, request):
        issues = ReportTable.objects.all()
        return render(request, "Administration/assignwork.html", {'issues': issues})
    def post(self, request):
        #form=AssignWorkForm(request.POST)
        #if form.is_valid():
            #form.save()
            return render('assignwork')


    
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
    
class editauthority(View):
    def get(self, request,id):
        obj = AuthorityTable.objects.get(LOGIN__id=id)
        return render(request, "Administration/editauthority.html", {'val' :obj} ) 
    def post(self, request,id):
        obj = AuthorityTable.objects.get(LOGIN__id=id)
        form= AuthorityForm(request.POST,instance=obj)
        if form.is_valid():
            f=form.save(commit=False)
            f.save()
            return redirect('manageauthority')

    
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
        reports = ReportTable.objects.filter(AUTHORITY_ID__LOGIN_id=request.session['lid'])
        print(request.session['lid'])
        return render(request, "Authority/authorityreport.html", {'val': reports})
    
class updatestatus(View):
    def post(self, request,assignment_id):
        status = request.POST.get('status')
        assignment = AssignWorkTable.objects.get(id=assignment_id)
        assignment.Status = status
        assignment.save()
        return redirect('authorityreport')
     
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
       
    

class AuthorityHome(View):
    def get(self, request):
        return render(request, "Authority/AuthorityHome.html") 
      
class LoginPage(APIView):
    def post(self,request):
        print("#################")
        response_dict={}

        username=request.data.get("username")
        password=request.data.get("password")
        print("$$$$$$$$$",username)

        if not username or not password:
            response_dict["message"]="failed"
            return Response(response_dict,status=status.HTTP_400_BAD_REQUEST)
        
        t_user=LoginTable.objects.filter(username=username).first()
        print("%%%%%%%%%%%%%%%%%%",t_user)

        if not t_user:
            response_dict["message"]="failed"
            return Response(response_dict,status=status.HTTP_401_UNAUTHORIZED)
        
        else:
            response_dict["message"]="failed"
            response_dict["login_id"]=t_user.id
        return Response(response_dict,status=HTTP_200_ok)
    

class UserReg_api(APIView):
    def post(self,request):
        print("#################",request.data)

        user_serial= User_Serializer(data=request.data)
        login_serial=Login_Serializer(data=request.data)

        data_valid=user_serial.is_valid()
        login_valid=login_serial.is_valid()

        if data_valid and login_valid:
            login_profile=login_serial.save(usertype='USER')

            user_serial.save(login=login_profile)

            return Response(user_serial.data, status=status.HTTP_201_CREATED)






            