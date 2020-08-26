from django.shortcuts import render
import rest_framework
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from . forms import PredictionForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from . models import prediction
from .serializers import predictionSerializers
import joblib
import pickle
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from collections import defaultdict,Counter


class PredictionView(viewsets.ModelViewSet):
    queryset = prediction.objects.all()
    serializer_class = predictionSerializers



def approvereject(unit):
    try:
        mdl = joblib.load("C:/Users/AYUTI/Desktop/Django/DjangoAPI/MyAPI/Pickle_Prediction_Model.pkl")

        scalers = joblib.load("C:/Users/AYUTI/Desktop/Django/DjangoAPI/MyAPI/scalers1.pkl")
        X = scalers.transform(unit)
        y_pred = mdl.predict(X)
        y_pred = (y_pred > 0.22)
        temp={}
        temp[' ']=y_pred
        newdf=pd.DataFrame({' ':temp}).transpose() #newdf = pd.DataFrame(y_pred, column=[status])
        newdf = newdf.replace({True: 'Possibility that you might have diabetes.', False: 'You are SAFE.'})
        return (' {}'.format(newdf))
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def index(request):
    if request.method=='POST':
        form=PredictionForm(request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data['Firstname']
            Lastname=form.cleaned_data['Lastname']
            Pregnancies=form.cleaned_data['Pregnancies']
            Glucose = form.cleaned_data['Glucose']
            BloodPressure = form.cleaned_data['BloodPressure']
            Insulin = form.cleaned_data['Insulin']
            BMI = form.cleaned_data['BMI']
            Age = form.cleaned_data['Age']
            temp={}
            temp['A'] = request.POST.get('Pregnancies')
            temp['B'] = request.POST.get('Glucose')
            temp['C'] = request.POST.get('BloodPressure')
            temp['D'] = request.POST.get('Insulin')
            temp['E'] = request.POST.get('BMI')
            temp['F'] = request.POST.get('Age')

            df=pd.DataFrame({'x':temp}).transpose()
           # print(df)
            answer=approvereject(df)
           # print(answer)
            messages.success(request,'Applicant Status: {}'.format(answer))

    form=PredictionForm(request.POST or None)
    context = {'form': form, 'A': 'Pregnancies','B': 'Glucose', 'C': 'BloodPressure', 'D': 'Insulin', 'E': 'BMI', 'F':'AGE'}


    return render(request, 'index.html', context)

