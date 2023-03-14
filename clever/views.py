from django.shortcuts import render
from .models import signup,Test,CPTest
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib import auth
def index(request):

    if 'uid'in request.session:
       uid=request.session['uid']
       userrecord=signup.objects.get(id=uid)
       username=userrecord.Name
       context={'usernm':username}
       return render(request,'clever/index.html',context)
    else:
       return render(request,'clever/index.html',{})
def reg(request):
    if request.method=='POST':
        data1 = request.POST.get('nm','')
        data2 = request.POST.get('em', '')
        data3 = request.POST.get('ph', '')
        data4 = request.POST.get('us', '')
        data5 = request.POST.get('ps', '')
        data6 = request.POST.get('dob', '')
        data7 = request.POST.get('cty', '')
        data8 = request.POST.get('st','')
        song_obj = signup(Name=data1, Email=data2, Phone=data3, Username=data4, Password=data5, DOB=data6, City=data7, State=data8)
        song_obj.save()
        return render(request, 'clever/index.html')
    else:
        return render(request, 'clever/index.html')
def login(request):
    if request.method == 'POST':
        Uss = request.POST['us']
        Pss = request.POST['ps']
        try:
            d1 = signup.objects.get(Username=Uss)
            d2 = signup.objects.get(Password=Pss)
        except signup.DoesNotExist:
            d1 = None
            d2 = None
            if (Uss == d1 and Pss == d2):
              return render(request, 'clever/index.html')
            else:
               return render(request, 'clever/index.html')
        else:
            if (Uss == d1.Username and Pss == d2.Password):
                request.session['uid'] = d1.id
                return render(request, 'clever/index.html')
            else:
                return render(request, 'clever/index.html')
    return render(request, 'clever/index.html')

def logout(request):
    auth.logout(request)
    try:
        del request.session['userid']
    except KeyError:
        pass
    return render(request,'clever/index.html')
def C(request):
    return render(request, 'clever/C.html',{})
def CPP(request):
    return render(request, 'clever/CPP.html', {})
def DataStructure(request):
    return render(request, 'clever/DataStructure.html', {})
def OperatingSystem(request):
    return render(request, 'clever/OperatingSystem.html', {})
def Practice(request):
    return render(request, 'clever/Practice.html', {})
def contact(request):
    return render(request, 'clever/contact.html',{})
def ProgramStructure(request):
    return render(request, 'clever/ProgramStructure.html', {})
def BasicSyntax(request):
    return render(request, 'clever/BasicSyntax.html', {})
def DataTypes(request):
    return render(request, 'clever/DataTypes.html', {})
def Variables(request):
    return render(request, 'clever/Variables.html', {})
def Constants(request):
    return render(request, 'clever/Constants.html', {})
def StorageClass(request):
    return render(request, 'clever/StorageClass.html', {})
def Operators(request):
    return render(request, 'clever/Operators.html', {})
def DecisionMaking(request):
    return render(request, 'clever/DecisionMaking.html', {})
def Loops(request):
    return render(request, 'clever/Loops.html', {})
def Functions(request):
    return render(request, 'clever/Functions.html', {})
def ScopeRules(request):
    return render(request, 'clever/ScopeRules.html', {})
def Arrays(request):
    return render(request, 'clever/Arrays.html', {})
def Pointers(request):
    return render(request, 'clever/Pointers.html', {})
def Strings(request):
    return render(request, 'clever/Strings.html', {})
def Structures(request):
    return render(request, 'clever/Structures.html', {})
def Unions(request):
    return render(request, 'clever/Unions.html', {})
def BitField(request):
    return render(request, 'clever/BitField.html', {})
def EnvironmentSetup(request):
    return render(request, 'clever/EnvironmentSetup.html', {})
def DSLinkList(request):
    return render(request, 'clever/DSLinkList.html', {})
def DStack(request):
    return render(request, 'clever/DStack.html', {})
def DSQueue(request):
    return render(request, 'clever/DSQueue.html', {})
def DSBTree(request):
    return render(request, 'clever/DSBTree.html', {})
def DSHeap(request):
    return render(request, 'clever/DSHeap.html', {})
def DSBSTree(request):
    return render(request, 'clever/DSBSTree.html', {})
def DSHashing(request):
    return render(request, 'clever/DSHashing.html', {})
def DSGraph(request):
    return render(request, 'clever/DSGraph.html', {})
def DSMatrix(request):
    return render(request, 'clever/DSMatrix.html', {})
def cpHome(request):
    return render(request, 'clever/cpHome.html', {})
def cpEnvironmentSetup(request):
    return render(request, 'clever/cpEnvironmentSetup.html', {})
def cpBasicSyntax(request):
    return render(request, 'clever/cpBasicSyntax.html', {})
def cpComments(request):
    return render(request, 'clever/cpComments.html', {})
def cpDataTypes(request):
    return render(request, 'clever/cpDataTypes.html', {})
def cpVariableTypes(request):
    return render(request, 'clever/cpVariableTypes.html', {})
def cpVariableScope(request):
    return render(request, 'clever/cpVariableScope.html', {})
def cpConstantsLiterals(request):
    return render(request, 'clever/cpConstantsLiterals.html', {})
def cpModifierTypes(request):
    return render(request, 'clever/cpModifierTypes.html', {})
def cpStorageClasses(request):
    return render(request, 'clever/cpStorageClasses.html', {})
def cpOperators(request):
    return render(request, 'clever/cpOperators.html', {})
def cpLoopTypes(request):
    return render(request, 'clever/cpLoopTypes.html', {})
def cpDecisionMaking(request):
    return render(request, 'clever/cpDecisionMaking.html', {})
def cpFunctions(request):
    return render(request, 'clever/cpFunctions.html', {})
def cpNumbers(request):
    return render(request, 'clever/cpNumbers.html', {})
def cpArrays(request):
    return render(request, 'clever/cpArrays.html', {})
def AI(request):
    return render(request, 'clever/AI.html', {})
def MachineLearning(request):
    return render(request, 'clever/MachineLearning.html', {})
def EH(request):
    return render(request, 'clever/EH.html', {})
def BigData(request):
    return render(request, 'clever/BigData.html', {})



# Create your views here.
def cresult(request):
    if request.method=='POST':
        data1 = request.POST.get('qn',  '')
        data2 = request.POST.get('qn1', '')
        data3 = request.POST.get('qn2', '')
        data4 = request.POST.get('qn3', '')
        data5 = request.POST.get('qn4', '')
        data6 = request.POST.get('qn5', '')
        data7 = request.POST.get('qn6', '')
        data8 = request.POST.get('qn7', '')
        data9 = request.POST.get('qn8', '')
        data10= request.POST.get('qn9','')
        #song_obj = signup(Name=data1, Email=data2, Phone=data3, Username=data4, Password=data5, DOB=data6, City=data7, State=data8)
        #song_obj.save()
        t1=Test.objects.all()
        li=[]

        userans=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
        #return HttpResponse(userans)
        li=[]
        for i in t1:
            li.append(i.Answers)
        #return HttpResponse(li)
        cou=0
        b1=[]

        for i in range(0,10):
            if(userans[i]==li[i]):
                cou = cou+1
                b1.append(i+1)

        #if userans[8] == li[8]:


        if cou>=8:
            a=("Excellent")
        elif cou==7:
            a=("Good")
        elif cou<=6:
            a=("Fail")
        return render(request, 'clever/cresult.html',{'totalcorrectans':cou,'correctans':b1,'wrongans':10-cou,'result':a})
    else:
        return render(request, 'clever/Practice1.html')
def cpresult(request):
    if request.method=='POST':
        data1 = request.POST.get('q1', '')
        data2 = request.POST.get('q2', '')
        data3 = request.POST.get('q3', '')
        data4 = request.POST.get('q4', '')
        data5 = request.POST.get('q5', '')
        data6 = request.POST.get('q6', '')
        data7 = request.POST.get('q7', '')
        data8 = request.POST.get('q8', '')
        data9 = request.POST.get('q9', '')
        data10=request.POST.get ('q10','')
        #song_obj = signup(Name=data1, Email=data2, Phone=data3, Username=data4, Password=data5, DOB=data6, City=data7, State=data8)
        #song_obj.save()
        t1 = CPTest.objects.all()
        li = []

        userans = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]
        li = []
        for i in t1:
            li.append(i.Answers)
        cou = 0
        b1 = []

        for i in range(0, 10):
          if (userans[i] == li[i]):
            cou = cou + 1
            b1.append(i + 1)
    # return HttpResponse(b1)
        if cou>=8:
            a=("Excellent")
        elif cou==7:
            a=("Good")
        elif cou<=6:
            a=("Fail")
        return render(request, 'clever/cpresult.html', {'totalcorrectans': cou, 'correctans': b1,'wrongans':10-cou,'result':a})
    else:
          return render(request, 'clever/Practice1.html')
def Search(request):
    if request.method == 'POST':
        data1 = request.POST.get('search', '')
        if data1=='c':
            return render(request, 'clever/C.html', {})
        elif data1=='AI':
            return render(request, 'clever/AI.html', {})
        elif data1=='binary tree':
            return render(request, 'clever/DSBTree.html', {})
        elif data1=='machine learning':
            return render(request, 'clever/MachineLearning.html', {})
        elif data1 == 'LinkList':
            return render(request, 'clever/DSLinkList.html', {})
        elif data1=='numbers in c++':
            return render(request, 'clever/cpNumbers.html', {})
        elif data1=='operators in c++':
            return render(request, 'clever/cpOperators.html', {})
        elif data1=='functions in c':
            return render(request, 'clever/Functions.html', {})
        elif data1 == 'environment setup in c++':
            return render(request, 'clever/cpEnvironmentSetup.html', {})
        elif data1=='loop in c++':
            return render(request, 'clever/cpLoopTypes.html', {})
        elif data1 == 'operators in c':
            return render(request, 'clever/Operators.html', {})
        elif data1=='heap':
            return render(request, 'clever/DSHeap.html', {})
        elif data1 == 'BitField':
            return render(request, 'clever/BitField.html', {})
        elif data1 == 'pointers':
            return render(request, 'clever/Pointers.html', {})
        elif data1 == 'program structure':
            return render(request, 'clever/ProgramStructure.html', {})
        elif data1 == 'scope rules':
            return render(request, 'clever/ScopeRules.html', {})
        elif data1 == 'storage class':
            return render(request, 'clever/StorageClass.html', {})
        elif data1 == 'string':
            return render(request, 'clever/Strings.html', {})
        elif data1 == 'structure':
            return render(request, 'clever/Structures.html', {})
        elif data1 == 'union':
            return render(request, 'clever/Unions.html', {})
        elif data1 == 'stack':
            return render(request, 'clever/DStack.html', {})
        elif data1=='ethical hacking':
            return render(request, 'clever/EH.html', {})
        elif data1=='matrix':
            return render(request, 'clever/DSMatrix.html', {})
        elif data1=='environment setup in c':
            return render(request, 'clever/EnvironmentSetup.html', {})
        elif data1=='decision making in c':
            return render(request, 'clever/DecisionMaking.html', {})
        elif data1=='storage classes in c++':
            return render(request, 'clever/cpStorageClasses.html', {})
        elif data1=='variable in c++':
            return render(request, 'clever/cpVariableScope.html', {})
        elif data1=='variable in c':
            return render(request, 'clever/Variables.html', {})
        elif data1=='hashing':
            return render(request, 'clever/DSHashing.html', {})
        elif data1=='c++':
            return render(request, 'clever/cpHome.html', {})
        elif data1=='queue':
            return render(request, 'clever/DSQueue.html', {})
        elif data1=='variable types in c++':
            return render(request, 'clever/cpVariableTypes.html', {})
        elif data1=='binary search in c++':
            return render(request, 'clever/DSBSTree.html', {})
        elif data1=='data types in c++':
            return render(request, 'clever/cpDataTypes.html', {})
        elif data1=='Constant in c++':
            return render(request, 'clever/cpConstantsLiterals.html', {})
        elif data1 == 'graph':
            return render(request, 'clever/DSGraph.html', {})
        elif data1=='modifier in c++':
            return render(request, 'clever/cpModifierTypes.html', {})
        elif data1=='data types in c':
            return render(request, 'clever/DataTypes.html', {})
        elif data1 == 'decision making in c++':
            return render(request, 'clever/cpDecisionMaking.html', {})
        elif data1=='comments in c++':
            return render(request, 'clever/cpComments.html', {})
        elif data1=='Basic Syntax C++':
            return render(request, 'clever/cpBasicSyntax.html', {})
        elif data1=='Constants':
            return render(request, 'clever/Constants.html', {})
        elif data1 == 'BigData':
            return render(request, 'clever/BigData.html', {})
        elif data1=='Arrays':
            return render(request, 'clever/Arrays.html', {})
        elif data1=='DS':
            return render(request, 'clever/DataStructure.html', {})
        elif data1=='Array in C++':
            return render(request, 'clever/cpArrays.html', {})
        elif data1=='OS' or 'Operating System':
            return render(request, 'clever/OperatingSystem.html', {})
    else:
        return render(request, 'clever/index.html', {})
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
def contribute(request):
  paypal_dict={
       "business":"jatind569@gmail.com",
       "amount":"01.00",
       #"currency_code":"INR",
       "item_name":"Jot's LIVER",
        "invoice":"unique-invoice-0001",
        "notify_url":"localhost:80000/a-very-hard-to-guess-url/",
        "return_url":"localhost:80000/paypal-return/",
        "cancel_return":"localhost:80000/paypal-cancel/",
     }
  form=PayPalPaymentsForm(initial=paypal_dict)
  context={"form":form}
  return render_to_response('clever/contribute.html',context)
@csrf_exempt
def paypal_return(request):
   args={'post':request.POST,'get':request.GET}
   return render_to_response('clever/paypal_return.html',args)
def paypal_cancel(request):
   args={'post':request.POST,'get':request.GET}
   return render_to_response('clever/paypal_cancel.html',args)































