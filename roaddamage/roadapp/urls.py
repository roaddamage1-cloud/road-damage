
from django.contrib import admin
from django.urls import include, path

from roadapp.views import *

urlpatterns = [
    # /////////////////////////////////////// Administration //////////////////////////////

    path('', login.as_view(), name='login'),
    path('addauthority', addauthority.as_view(), name='addauthority'),
    path('complaint', complaint.as_view(), name='complaint'), 
    path('viewassignAdmin', viewassignAdmin.as_view(), name='viewassignAdmin'), 
    path('authorityDep',authorityDep.as_view(), name='authorityDep' ),
    
    path('detection', detection.as_view(), name='detection'), 
    path('feedback', feedback.as_view(), name='feedback'), 
    path('issues', issues.as_view(), name='issues'), 
    path('manageauthority', manageauthority.as_view(), name='manageauthority'),
    path('deleteauthority/<int:lid>', deleteauthority.as_view(), name='deleteauthority'),
    path('manageuser', manageuser.as_view(), name='manageuser'), 
    path('deleteuser/<int:lid>', deleteuser.as_view(), name='deleteuser'),
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
