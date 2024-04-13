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
    

   

]