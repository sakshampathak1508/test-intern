from urllib import response
from django.shortcuts import render
import requests
import json
from .models import Restaurant,Hour
from.serializers import ResSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def myfunc(request):
    for i in range(1,5):
        r = requests.get('https://random-data-api.com/api/restaurant/random_restaurant',params=request.GET)
        r = r.json()
        for item,key in enumerate(r['hours']):
            print(key,item)
            obj_hour = Hour(day=key,open_time=item['opens_at'],close_time=item['close_at'],is_closed=item['is_closed'])
            obj_hour.save() 
        print(r)
        obj = Restaurant(id=r['id'],name=r['name'],res_type=r['type'],desc=r['description'],hours=obj_hour.id)
        obj.save()

class myapiview(APIView):
    def get(self,request,*args,**kwargs):
        res_type = request.GET.get('type','')
        time = request.GET.get('time','')
        date = request.GET.get('date','')
        obj = Restaurant.objects.filter(res_type=res_type)
        output_data =''
        if obj:
            for i in obj:
                if i.hours.day==date.day and (time>=i.hours.open_time and time<=i.hours.close_time):
                    ser = ResSerializer(i,many=True)
                    if ser.is_valid():
                        output_data.append(i)
        return Response(output_data) 
        