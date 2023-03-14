"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import views
urlpatterns = [
  url(r'^$', views.index,name="index1"),
  url(r'^contact/$',views.contact,name='Contact1'),
  url(r'^registration/$',views.reg,name='reg1'),
  url(r'^login/$', views.login, name='login1'),
  url(r'^logout/$', views.logout, name='logout1'),
  url(r'^C/$', views.C, name='C1'),
  url(r'^CPP/$', views.CPP , name='CPP1'),
  url(r'^DataStructure/$', views.DataStructure , name='DataStructure1'),
  url(r'^OperatingSystem/$', views.OperatingSystem , name='OperatingSystem1'),
  url(r'^Practice/$', views.Practice , name='Practice1'),
  url(r'^ProgramStructure/$', views.ProgramStructure, name='ProgramStructure1'),
  url(r'^BasicSyntax/$', views.BasicSyntax, name='BasicSyntax1'),
  url(r'^DataTypes/$', views.DataTypes, name='DataTypes1'),
  url(r'^Variables/$', views.Variables, name='Variables1'),
  url(r'^Constants/$', views.Constants, name='Constants1'),
  url(r'^StorageClass/$', views.StorageClass, name='StorageClass1'),
  url(r'^Operators/$', views.Operators, name='Operators1'),
  url(r'^DecisionMaking/$', views.DecisionMaking, name='DecisionMaking1'),
  url(r'^Loops/$', views.Loops, name='Loops1'),
  url(r'^Functions/$', views.Functions, name='Functions1'),
  url(r'^ScopeRules/$', views.ScopeRules, name='ScopeRules1'),
  url(r'^Arrays/$', views.Arrays, name='Arrays1'),
  url(r'^Pointers/$', views.Pointers, name='Pointers1'),
  url(r'^Strings/$', views.Strings, name='Strings1'),
  url(r'^Structures/$', views.Structures, name='Structures1'),
  url(r'^Unions/$', views.Unions, name='Unions1'),
  url(r'^BitField/$', views.BitField, name='BitField1'),
  url(r'^EnvironmentSetup/$', views.EnvironmentSetup, name='EnvironmentSetup1'),
  url(r'^DSLinkList/$', views.DSLinkList, name='DSLinkList1'),
  url(r'^DStack/$', views.DStack, name='DStack1'),
  url(r'^DSQueue/$', views.DSQueue, name='DSQueue1'),
  url(r'^DSBTree/$', views.DSBTree, name='DSBTree1'),
  url(r'^DSBSTree/$', views.DSBSTree, name='DSBSTree1'),
  url(r'^DSHeap/$', views.DSHeap, name='DSHeap1'),
  url(r'^DSHashing/$', views.DSHashing, name='DSHashing1'),
  url(r'^DSGraph/$', views.DSGraph, name='DSGraph1'),
  url(r'^DSMatrix/$', views.DSMatrix, name='DSMatrix1'),
  url(r'^cpHome/$', views.cpHome , name='cpHome1'),
  url(r'^cpEnvironmentSetup/$', views.cpEnvironmentSetup , name='cpEnvironmentSetup1'),
  url(r'^cpBasicSyntax/$', views.cpBasicSyntax , name='cpBasicSyntax1'),
  url(r'^cpComments/$', views.cpComments , name='cpComments1'),
  url(r'^cpDataTypes/$', views.cpDataTypes , name='cpDataTypes1'),
  url(r'^cpVariableTypes/$', views.cpVariableTypes, name='cpVariableTypes1'),
  url(r'^cpVariableScope/$', views.cpVariableScope, name='cpVariableScope1'),
  url(r'^cpConstantsLiterals/$', views.cpConstantsLiterals, name='cpConstantsLiterals1'),
  url(r'^cpModifierTypes/$', views.cpModifierTypes, name='cpModifierTypes1'),
  url(r'^cpStorageClasses/$', views.cpStorageClasses, name='cpStorageClasses1'),
  url(r'^cpOperators/$', views.cpOperators, name='cpOperators1'),
  url(r'^cpLoopTypes/$', views.cpLoopTypes, name='cpLoopTypes1'),
  url(r'^cpDecisionMaking/$', views.cpDecisionMaking, name='cpDecisionMaking1'),
  url(r'^cpFunctions/$', views.cpFunctions, name='cpFunctions1'),
  url(r'^cpNumbers/$', views.cpNumbers, name='cpNumbers1'),
  url(r'^cpArrays/$', views.cpArrays, name='cpArrays1'),
  url(r'^AI/$', views.AI, name='AI1'),
  url(r'^MachineLearning/$', views.MachineLearning, name='MachineLearning1'),
  url(r'^BigData/$', views.BigData, name='BigData1'),
  url(r'^EH/$', views.EH, name='EH1'),
  url(r'^cresult/$', views.cresult, name='cr'),
  url(r'^cpresult/$', views.cpresult, name='cpr'),
  url(r'^Search/$', views.Search, name='Search1'),
  url(r'^contribute/$', views.contribute, name='contribute1'),
  url(r'^paypal-return/$', views.paypal_return),
  url(r'^paypal-cancel/$', views.paypal_cancel),
  url(r'^a-very-hard-to-guess-url/', include('paypal.standard.ipn.urls')),

]

