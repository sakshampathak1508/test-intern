from urllib import response
from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from .models import Restaurant
from.serializers import ResSerializer
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

def myfunc(request):
    for i in range(1,5):
        for i in range(1,101):
            r = requests.get('https://random-data-api.com/api/restaurant/random_restaurant',params=request.GET)
            r = r.json()
            for item in r['hours']:
                # print(r['hours'][item]['opens_at'])
                name = item
                res_name = r['name']
                res_type = r['type']
                res_desc = r['description']
                opens_at =  r['hours'][item]['opens_at']
                closes_at = r['hours'][item]['closes_at']
                is_closed = r['hours'][item]['is_closed']
                obj = Restaurant(name=res_name,res_type=res_type,desc=res_desc,day=name,open_time=opens_at,close_time=closes_at,is_closed=is_closed)
                obj.save() 
        return HttpResponse('success')

class myapiview(APIView):
    def get(self,request,*args,**kwargs):
        res_type = request.GET.get('type','')
        time = request.GET.get('time','')
        date = request.GET.get('date','')
        day = datetime.strptime(date, '%d-%m-%Y').strftime('%A')
        day = day.lower()
        time = datetime.strptime(time, '%H:%M:%S').time()
        obj = list(Restaurant.objects.filter(res_type=res_type,day=day))
        # print(obj)
        output_data =[]
        if obj:
            for i in obj:
                # print(i)
                if time>=i.open_time and time<=i.close_time:
                    ser = ResSerializer(i).data
                    output_data.append(ser)
            return Response(output_data) 
        