from MyApp import models
from django import forms

class createform(forms.ModelForm):
    class Meta:
        model = models.m_create
        fields = ['name','Address','CurrentLoactio','mobilenumber',]

class readid(forms.Form):
    id = forms.IntegerField()


class updateform(forms.ModelForm):
    class Meta:
        model = models.m_create
        fields = ['id','name','Address','CurrentLoactio','mobilenumber']
