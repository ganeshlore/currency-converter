from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from google_currency import convert
import json  
# Create your views here.
def convert_currency(request):
  # Get Params
  from_country  = request.GET.get('from')
  to_country    = request.GET.get('to')
  amount        = request.GET.get('amount')
  data = convert(from_country if from_country else 'usd',
           to_country if to_country else 'inr',
           int(amount) if amount is not None and amount .isnumeric() else 1)
  return JsonResponse(json.loads(data))
