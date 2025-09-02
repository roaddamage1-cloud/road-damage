
from django.contrib import admin
from django.urls import include, path

from roadapp.views import AdminHome, AuthorityHome, addauthority, alert, assignwork, authorityreport, complaint, detection, fdback, feedback, issues, login, manageauthority, manageuser, report, sendissues, update, updatingstatus, viewassign, viewissues

urlpatterns = [
    # /////////////////////////////////////// Administration //////////////////////////////

    path('', login.as_view(), name='login'),
    path('addauthority', addauthority.as_view(), name='addauthority'),
    path('assignwork', assignwork.as_view(), name='assignwork'), 
    path('complaint', complaint.as_view(), name='complaint'), 
    path('detection', detection.as_view(), name='detection'), 
    path('feedback', feedback.as_view(), name='feedback'), 
    path('issues', issues.as_view(), name='issues'), 
    path('manageauthority', manageauthority.as_view(), name='manageauthority'),
    path('manageuser', manageuser.as_view(), name='manageuser'), 
    path('report', report.as_view(), name='report'),
    path('update/<int:id>', update.as_view(), name='update'), 

    path('AdminHome', AdminHome.as_view(), name='AdminHome'),

    # /////////////////////////////////////   Authority    //////////////////////////////////////
    
    path('alert', alert.as_view(), name='alert'), 
    path('authorityreport', authorityreport.as_view(), name='authorityreport'), 
    path('fdback', fdback.as_view(), name='fdback'), 
    path('sendissues', sendissues.as_view(), name='sendissues'), 
    path('viewassign', viewassign.as_view(), name='viewassign'), 
    path('viewissues', viewissues.as_view(), name='viewissues'), 
    path('AuthorityHome', AuthorityHome.as_view(), name='AuthorityHome')
]
