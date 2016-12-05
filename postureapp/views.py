# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from postureapp.models import Document, Recommendation, PickleObject
from postureapp.forms import DocumentForm
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from postureapp.serializers import DocumentSerializer, UserSerializer, RecommendationSerializer, PickleObjectSerializer

from rest_framework import viewsets
from django.contrib.auth.models import User

from datetime import datetime,timedelta
import datetime
from django.utils import timezone

from django.http import HttpResponse
import numpy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pickle

import csv
from boto.s3.connection import S3Connection

def index(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            document = Document(docfile=request.FILES['docfile'])
            document.save()
            
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('index'))
            return HttpResponse("Recommendation will be here")
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

# Render list page with the documents and the form
    return render(
              request,
              'index.html',
              {'documents': documents, 'form': form}
              )

def dashboard(request):
    # Handle file upload
    
    doc= Document.objects.order_by('-id')[0]
    
    goodlist = Recommendation.objects.filter(repstatus = True)
    goodsize = len(goodlist)
    
    badlist = Recommendation.objects.filter(repstatus = False)
    badsize = len(badlist)
    
    if goodsize ==0 and badsize ==0:
        goodsize=1;
    
    enddate = datetime.datetime.now()
    startdate = enddate - timedelta(days=6)
    monday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=2))
    tuesday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=3))
    wednesday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=4))
    thursday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=5))
    friday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=6))
    saturday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=7))
    sunday = len(Recommendation.objects.filter(pub_date__range=[startdate, enddate]).filter(pub_date__week_day=1))

    weeklist = [sunday, monday, tuesday, wednesday, thursday, friday, saturday]
# Render list page with the documents and the form
    return render(
              request,
                  'dashboard.html',{'doc' : doc, 'goodsize' : goodsize, 'badsize' : badsize, 'weeklist' : weeklist}
              )

def about(request):
# About page
   
    return render(
              request,
              'about.html'
              )

def report(request):
# Report Page
    conn = S3Connection(key, password)
    mybucket = conn.get_bucket('classifiermodel')
    key = mybucket.get_key('FinalReportPostureTrainer.pdf')
    key.get_contents_to_filename(key.name)
    with open(key.name, 'rb') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=FinalReportPostureTrainer'
    
    return response

def team(request):
# Handle file upload


# Render list page with the documents and the form
    return render(
              request,
              'team.html'
              )

class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Document.objects.all().order_by('-pub_date')
    serializer_class = DocumentSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all().order_by('-pub_date')
    serializer_class = RecommendationSerializer

class PickleObjectViewSet(viewsets.ModelViewSet):
    queryset = PickleObject.objects.all()
    serializer_class = PickleObjectSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def getrecommendation(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = Document(docfile=request.FILES['docfile'])
            document.save()
#return Response({document.pub_date})
   
    conn = S3Connection(key, password)
    mybucket = conn.get_bucket('classifiermodel')
    key = mybucket.get_key('kneighboursmodel.p')
    key.get_contents_to_filename(key.name)
    mlmodel = pickle.load(open( key.name, "rb" ) )

    doc= Document.objects.order_by('-id')[0].docfile
    doc.open(mode='r')
    data = numpy.genfromtxt(doc, delimiter=',')
    data = data[:,1:]
    prediction = mlmodel.predict(data)
    doc.close()
#url = doc.url

    #t, x, y, z, flex, mag = numpy.loadtxt(lines, delimiter=',', usecols=(0, 4), unpack=True)
#f = open(url)


#mylist = lines.splitlines()
    
    #for line in lines:

#currentline = line.split(b",")
        
#x = line.split(',')[0]

    if prediction.mean()>=0.5:
        recommendation = Recommendation.objects.create(repstatus=True)
        recommend = "True"
    else:
        recommendation = Recommendation.objects.create(repstatus=False)
        recommend = "False"
    return Response({recommendation.repstatus})

