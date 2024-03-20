from django.shortcuts import render
from MyApp import forms
from MyApp import models
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.contrib import messages
# from django.conf import coo
# Create your views here.
def registration(request):
    pass
def login(request):
    pass
def home(request):
    con = {"name" : "Ashish"}
    # obj = request.
    response = HttpResponse("Cookie Set") 
    response.set_cookie("java-tutorial", "ASHISHHH")
    return response
    # return render(request, 'Home.html', context= con)


 
def create(request):
    if request.method == 'POST':
        fm = forms.createform(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data["name"]
            Address = fm.cleaned_data["Address"]
            CurrentLoactio = fm.cleaned_data["CurrentLoactio"]
            mobilenumber = fm.cleaned_data["mobilenumber"]

            createobj = models.m_create(name=name,Address=Address,CurrentLoactio=CurrentLoactio,mobilenumber=mobilenumber)
            createobj.save()
            fm = forms.createform()
        else:
            print("please enert")
    else:
        fm = forms.createform()
    cont = {'createform':fm}
    return render(request, "insert.html", cont)

def read(request):
    print('Read')
    if request.method =='POST':
        view = models.m_create.objects.all()
        fm = forms.readid(request.POST)
        if fm.is_valid():
            rid = fm.cleaned_data["id"]
            try:
                specificrec = models.m_create.objects.get(pk = rid)
            except models.m_create.DoesNotExist:
                # return HttpResponse("id not exist")
                mess2 = messages.add_message(request,messages.SUCCESS, message= "invilid ID")
                cont ={'views':view, 'form':fm, 'message':mess2}
                return render(request, 'view.html',cont)
            
        else: 
            specificrec = None
    else:
        view = models.m_create.objects.all()
        fm = forms.readid()
        specificrec = None
    cont ={'views':view, 'form':fm, 'singledata':specificrec}
    return render(request, 'view.html',cont)

def update(request):
    if request.method =="POST":
        fm = forms.updateform(request.POST)
        if fm.is_valid():
            id = request.POST['myid']
            try:
                data = models.m_create.objects.get(pk=id)
                print(data)
            except models.m_create.DoesNotExist:
                messagess = messages.add_message(request, messages.ERROR, message="ID NOT PRESENT")
                fm = forms.updateform()
                cont = {'form': fm, "ashish":messagess}
                return render(request,'update.html', cont)
            name = fm.cleaned_data["name"]
            address = fm.cleaned_data["Address"]
            currentlocation = fm.cleaned_data["CurrentLoactio"]
            mobile = fm.cleaned_data["mobilenumber"]

            s = models.m_create(id=id,name=name,Address=address,CurrentLoactio=currentlocation,mobilenumber=mobile)
            s.save()
            fm = forms.updateform()
        else: 
            print('data is invilid')
    else:
        fm = forms.updateform()
    cont = {'form': fm}
    return render(request,'update.html', cont)

def delete(request):
    if request.method == 'POST':
        id = request.POST["id"]
        try:
            data = models.m_create.objects.get(pk = id)
            s=models.m_create(id = id)
            s.delete()
            message=messages.add_message(request, messages.SUCCESS,message="record found and below data is deleted")
        except models.m_create.DoesNotExist:
            message=messages.add_message(request, messages.SUCCESS,message="INVALID ID PASSED")
            data = None
        cont = {'cont':data, "messages":message}

        return render(request,'delete.html',cont)

    return render(request,'delete.html')
    


