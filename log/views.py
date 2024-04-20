from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import User, cList, cVisit, visitCategory
from datetime import datetime, timedelta



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
  
        activeItems = cList.objects.order_by("cOwner").all()
        
        
    
        return render(request, "incoms/cLogs.html",{
            "activeItems":activeItems,
            
            
        })


def newEntry(request):
  return render(request, "incoms/newEntry.html")

def newCEtry(request):

    if request.method == "POST":
        loggedUser = request.user
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
            cTechnician = loggedUser
            
        )
        # We save the new object to our database
        newItem.save()

        return HttpResponseRedirect(reverse(cLogs))
    
def itemview(request, id):
    
    #id is byDefault the primary key in Django (i can change it if i want)
    itemDetails = cList.objects.get(id = id)
    loggedUser = request.user
    visitDetails = cList.objects.get(id = id)
    visit = cVisit.objects.filter(itemDetails = itemDetails).order_by('visitDate')
      
    return render(request, "incoms/itemview.html", {

        
        "itemDetails":itemDetails,
        "visits":visit,
        "visitDetails":visitDetails,
        "loggedUser":loggedUser
                
    })

def search(request):
    # Check if the request is a post request.-
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['q']
        # Filter your model by the search query
        results = cList.objects.filter(cOwner__contains=search_query.upper())
        return render(request, 'incoms/search.html', {'query':search_query, 'results':results})
        # return HttpResponse("Ok")
    else:
        return HttpResponse("NO ENTRIES")
    

def editEntry(request, id):
        
        itemDetails = cList.objects.get(id = id)
        
        
        return render(request, "incoms/editEntry.html", {
            "itemDetails": itemDetails,
            
        })

def editVisit(request, id):
        
        
        visitDetails = cVisit.objects.get(id = id)
        
        return render(request, "incoms/editVisit.html", {
            
            "visitDetails":visitDetails
            
        })

# --------------- EDITS ---------------
def saveEdit(request, id):
        itemDetails = cList.objects.get(id = id)
        

        itemDetails.cOwner = request.POST["customer"]
        itemDetails.cModel = request.POST["model"]
        itemDetails.cSerial = request.POST["serial"]
        itemDetails.cBuyDate = request.POST["sDate"]
        itemDetails.save()
        
        return HttpResponseRedirect(reverse(itemview, args=(id, ))) 

def saveEditVisit(request, id):
    
    visitDetails = cVisit.objects.get(id = id)

    # visitDetails.visitDate = request.POST["vDate"]
    visitDetails.loadHours = request.POST["vLoad"]
    visitDetails.workingHours = request.POST["vHours"]
    visitDetails.cNotes = request.POST["vNotes"]
    # visitDetails.visitReason = request.POST["category"]
    visitDetails.save()

    return HttpResponseRedirect(reverse(cLogs))
    


def newVisit(request, id):
    if request.method == "GET":
        itemDetails = cList.objects.get(id = id)
        allCategories = visitCategory.objects.all()

        return render(request, "incoms/newVisit.html", {
        "categories":allCategories,
        "itemDetails": itemDetails
        })

   
def saveVisit(request, id):
    itemDetails = cList.objects.get(id = id)
    
    vCategory = request.POST['category']
    vDate = request.POST['vDate']
    vLoad = request.POST['vLoad']
    vHours = request.POST['vHours']
    vNotes = request.POST['vNotes']

    categoryInstance =  visitCategory.objects.get(visitReason = vCategory)

    visit = cVisit(
        visitReason = categoryInstance,
        visitDate = vDate,
        itemDetails = itemDetails,
        loadHours = vLoad,
        workingHours = vHours,
        cNotes = vNotes,
    )

    visit.save()
    
    return HttpResponseRedirect(reverse(itemview, args=(id, ))) 
   
