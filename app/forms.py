from attr import attrs
from django import forms
from django.forms.fields import FileField
from django.forms.formsets import formset_factory
from django.forms.widgets import Textarea
import app.models as md
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class OfferProject(forms.Form):
    ProjectName = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Subject = forms.ModelChoiceField(queryset=md.Subject.objects.all(), widget=forms.Select(attrs={"class":"form-select"}))
    Summury = forms.CharField(widget=Textarea(attrs={"class":"form-control"}))
    Content = forms.CharField(widget=Textarea(attrs={"class":"form-control"}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class SearchProjects(forms.Form):
    InMyProjects = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={"class":"form-check-input"}))
    InProject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}), required=False)
    Author = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form-control"}))
    Subject = forms.ModelChoiceField(required=False,queryset=md.Subject.objects.all(),widget=forms.Select(attrs={"class":"form-select"}))

class CreateProject(forms.Form):
    ProjectName = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Subject = forms.ModelChoiceField(queryset=md.Subject.objects.all(), widget=forms.Select(attrs={"class":"form-select"}))
    Summury = forms.CharField(widget=Textarea(attrs={"class":"form-control"}))
    Content = forms.CharField(widget=Textarea(attrs={"class":"form-control"}))
    Users = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class CreateTask(forms.Form):
    TaskName = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    Content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    DateTo = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control"}))