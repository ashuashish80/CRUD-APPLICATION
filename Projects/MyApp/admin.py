from django.contrib import admin
from MyApp import models
# Register your models here.
@admin.register(models.m_create)
class modeladmin(admin.ModelAdmin):
    list_display = ['id','name','Address','CurrentLoactio','mobilenumber']
# admin.site.register(models.m_create, modeladmin)
