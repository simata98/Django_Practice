from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
  today = str(datetime.today().date())
  context = {"date":today}
  return render(request, 'foods/index.html', context=context)

def chicken(request):
  return render(request, 'foods/chicken.html')