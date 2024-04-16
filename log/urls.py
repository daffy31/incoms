from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("cLogs", views.cLogs,name="cLogs"),
    path("newEntry", views.newEntry, name="newEntry"),
    path("newCEtry", views.newCEtry, name="newCEtry"),
    path("itemview/<int:id>", views.itemview, name="itemview"),
    path("search", views.search, name="search"),
    path("editEntry/<int:id>", views.editEntry, name="editEntry"),
    path("saveEdit/<int:id>", views.saveEdit, name="saveEdit"),
    path("newVisit/<int:id>", views.newVisit, name="newVisit"),
    path("saveVisit/<int:id>", views.saveVisit, name="saveVisit"),
    

   

]