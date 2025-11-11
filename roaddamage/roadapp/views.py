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
            elif obj.UserType =='Authority':
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
        obj = Department.objects.all()
      # show all initially (or none if you prefer)
        return render(request, "Administration/report.html", {'object': obj})

    def post(self, request):
        dept = request.POST.get('deptname')
        obj = Department.objects.all()
        reports = ReportTable.objects.filter(DEPARTMENT_ID=dept)
        return render(request, "Administration/report.html", {'object': obj, 'val': reports})

    
class update_enddate(View):
    def post(self, request, report_id):
        date = request.POST.get('date')
        report = ReportTable.objects.get( id=report_id)

        # Check for existing assignment
        assign, created = AssignWorkTable.objects.get_or_create(REPORT_ID=report)

        if assign.Enddate:
            # Already assigned
            return HttpResponse('''<script>alert("End date already set!");window.location='/report'</script>''')

        assign.Enddate = date
        assign.Status = 'Pending'  # default status
        assign.save()
        return HttpResponse('''<script>alert("End date already set!");window.location='/report'</script>''')

class manageuser(View):
    def get(self, request):
        obj = UserTable.objects.all()
        return render(request, "Administration/manageuser.html", {'val': obj})
    
class deleteuser(View):
    def get(self, request, lid):
        obj = UserTable.objects.get(id=lid)
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

class deletereport(View):
    def get(self, request, lid):
        obj = ReportTable.objects.get(id=lid)
        obj.delete()
        return redirect('/report')

    
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
        dept=Department.objects.all()
        return render(request, "Administration/addauthority.html",{'dep':dept}) 
    def post(self, request):
        form= AuthorityForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.LOGIN = LoginTable.objects.create(Username=request.POST['Username'], Password=request.POST['Password'], UserType="Authority")
            f.save()
            return HttpResponse('''<script>alert("Added successfully!");window.location='/'</script>''')

        
class AdminHome(View):
    def get(self, request):
        return render(request, "Administration/AdminHome.html")
    
class department(View):
    def get(self, request):
        return render(request, "Administration/department.html")
    def post(self, request):
        form= departmentForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.save()
            return HttpResponse('''<script>alert("Added successfully!");window.location='/AdminHome'</script>''')
    
class updatedept(View):
    def post(self, request,assignment_id):
        status = request.POST.get('status')
        assignment = Department.objects.get(id=assignment_id)
        assignment.save()
        return redirect('department')


    
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
        obj = ReportTable.objects.all()
        for i in obj:
         print(i.Latitude, i.longitude)
        return render(request, "Authority/alert.html", {'val': obj} ) 
      
class ViewLocation(View):
    def get(self, request, id):
        report = ReportTable .objects.get(id=id)
        
        return render(request, "Authority/mapview.html", {'report': report})    
    
class alerts(View):
    def get(self, request):
        obj = ReportTable.objects.all()
        return render(request, "Authority/alerts.html", {'val': obj} )   

    
class fdback(View):
    def get(self, request):
        obj = FeedBackTable.objects.all()
        return render(request, "Authority/fdback.html", {'val': obj})   
    
class authorityreport(View):
    def get(self, request):
        obj = Department.objects.all()
      # show all initially (or none if you prefer)
        return render(request, "Authority/authorityreport.html", {'object': obj})

    def post(self, request):
        dept = request.POST.get('deptname')
        obj = Department.objects.all()
        reports = ReportTable.objects.filter(DEPARTMENT_ID=dept)
        return render(request, "Authority/authorityreport.html", {'object': obj, 'val': reports})
class update_status(View):
  def post(self,request, assignment_id):
    assign = AssignWorkTable.objects.get(id=assignment_id)
    if request.method == "POST":
        new_status = request.POST.get('status')
        if new_status:
            assign.Status = new_status
            assign.save()
        return HttpResponse('''<script>alert("updated successfully!");window.location='/authorityreport'</script>''')
 
    
    

     
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






            