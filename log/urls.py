from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("cLogs", views.cLogs,name="cLogs"),
    path("cLogs/newEntry", views.newEntry, name="cLogs/newEntry"),
    path("newCEtry", views.newCEtry, name="newCEtry"),
    path("cLogs/itemview/<int:id>", views.itemview, name="cLogs/itemview"),
    path("cLogs/search", views.search, name="cLogs/search"),
    path("editEntry/<int:id>", views.editEntry, name="editEntry"),
    path("editVisit/<int:id>", views.editVisit, name="editVisit"),
    path("saveEdit/<int:id>", views.saveEdit, name="saveEdit"),
    path("newVisit/<int:id>", views.newVisit, name="newVisit"),
    path("saveVisit/<int:id>", views.saveVisit, name="saveVisit"),
    path("saveEditVisit/<int:id>", views.saveEditVisit, name="saveEditVisit"),
    path("export_to_excel/<int:id>", views.export_to_excel, name="export_to_excel"),
    

   

]