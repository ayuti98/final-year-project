from django import forms
from django.forms import FloatField


class  PredictionForm(forms.Form):
    Firstname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname'}))
    Lastname = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname'}))
    Pregnancies = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Pregnancies'}))
    Glucose = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter value of Glucose'}))
    BloodPressure = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter value of BloodPressure'}))
    Insulin = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter value of Insulin'}))
    BMI = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter value of BMI'}))
    Age = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter value of Age'}))

