from django.shortcuts import render
import json
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .models import customer
from django.views.decorators.csrf import csrf_exempt

# Get all the customers from the database
def get_all_customers(request):
    data = serializers.serialize("json", customer.objects.all(), fields=('name','_id','email_address',"phone"))
    return JsonResponse(json.loads(data),safe=False)

# Get a single customer from the database using email or phone number as query filter
def get_customer_by_email_id_or_Phone(request, email_or_phone=""):
    data = serializers.serialize("json", customer.objects.filter(Q(email_address=email_or_phone) | Q(phone_number=email_or_phone)), fields=('name', '_id', 'email_address','phone_number'))
    return JsonResponse(json.loads(data),safe=False)

@csrf_exempt
def create_customer(request):
    if request.method =='POST':
        payload = json.loads(request.body)
        name = payload["name"]
        email_address = payload["email_address"]
        phone_number = payload["phone_number"]
        new_customer = customer(name=name,email_address=email_address,phone_number=phone_number)
        try:
            new_customer.save()
            response = json.dumps([{'Success':'Customer added successfully'}])
        except:
            response = json.dumps([{'Error':'Could not create account for customer'}])
        return JsonResponse(json.loads(response),safe=False)