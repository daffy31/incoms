from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, cList



# Create your views here.

def index(request):
    activeItems = cList.objects.all()
    
    return render(request, "incoms/index.html",{
        "activeItems":activeItems,
        
})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "incoms/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "incoms/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "incoms/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "incoms/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "incoms/register.html")
    
def cLogs(request):
  
        activeItems = cList.objects.all()
    
        return render(request, "incoms/cLogs.html",{
            "activeItems":activeItems,
            
        })


def newEntry(request):
  return render(request, "incoms/newEntry.html")

def newCEtry(request):

    if request.method == "POST":
        Vcustomer = request.POST["customer"]
        Vmodel = request.POST["model"]
        Vserial = request.POST["serial"]
        VsDate = request.POST["sDate"] #This goes to html name attr

        #Get Data to create instance cause it is a foreign key
        
        # Create new object from models
        # We set the previous variable to our model variable
        newItem= cList(
            cOwner = Vcustomer,
            cModel = Vmodel,
            cSerial = Vserial,
            cBuyDate = VsDate,
            
        )
        # We save the new object to our database
        newItem.save()

        return HttpResponseRedirect(reverse(cLogs))
    
def itemview(request, id):
    
    #id is byDefault the primary key in Django (i can change it if i want)
    itemDetails = cList.objects.get(id = id)
    
    return render(request, "incoms/itemview.html", {

        
        "itemDetails":itemDetails,
       
    })

def search(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['q']
        # Filter your model by the search query
        posts = cList.objects.filter(cOwner=search_query)
        return render(request, 'incoms/search.html', {'query':search_query, 'posts':posts})
        # return HttpResponse("Ok")
    else:
        return HttpResponse("NO ENTRIES")
    

def editEntry(request, id):
        activeItems = cList.objects.all()
        itemDetails = cList.objects.get(id = id)
        return render(request, "incoms/editEntry.html", {
            "itemDetails": itemDetails,
            "activeItems":activeItems,
        })

def saveEdit(request, id):
        itemDetails = cList.objects.get(id = id)
        itemDetails.cOwner = request.POST["customer"]
        itemDetails.cModel = request.POST["model"]
        itemDetails.cSerial = request.POST["serial"]
        itemDetails.save()
        return HttpResponseRedirect(reverse(cLogs))