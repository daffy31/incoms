from django.contrib import admin
from .models import User, cList, visitCategory, cVisit

# Register your models here.

admin.site.register(User)
admin.site.register(cList)
admin.site.register(visitCategory)
admin.site.register(cVisit)
