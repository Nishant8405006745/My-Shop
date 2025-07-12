from django.shortcuts import render,HttpResponse

from datetime import datetime
from home.models import Contact

# Create your views here.
"""def index(request):
    context={"variable":"This is Nishant kumar."}
    
    return render(request, "index.html",context)
    #return HttpResponse("This is my new website.")"""

def index(request):
    context={}
    return render(request, "index.html",context)

def about(request):
   return render(request, "about.html")
   
    #return HttpResponse("This is about page.")

def service(request):
    return render(request, "service.html") 
#    return HttpResponse("This is my service.")

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        text=request.POST.get("text")
        ncontact = Contact(name=name, mobile=mobile, email=email, text=text, )
        ncontact.save()
        
    return render(request, "contact.html") 
#    return HttpResponse("This is my contact page.")