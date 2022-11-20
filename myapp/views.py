import email
from email import message
import numbers
from socket import TCP_NODELAY
from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact

def index(request):
#context ={
#'variable': 'this is a variable value'}
    #message.success(request, "This is a test")
    return render(request,'index.html') 

def about(request):
    return render(request, 'about.html')

def rowhouse(request):
    return render(request,'rowhouse.html')

def getlawyer(request):
    return render(request,'getlawyer.html')   
    
def services(request):
   return render(request,'services.html')     

def contact(request):

    if request.method =='POST':
        name = request.POST.get('name') 
        email = request.POST.get('email') 
        phone = request.POST.get('phone') 
        desc = request.POST.get('desc') 
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')