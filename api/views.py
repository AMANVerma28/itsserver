from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets, status
from .models import *
from .serializers import *

# Create your views here.

#View method for model Household
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def householddetail(request):
#    List all Farms detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Household.objects.all()   
        serializer = HouseholdSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Farm
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def farmdetail(request):
#    List all Farms detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Farm.objects.all()   
        serializer = FarmSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Season
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def seasondetail(request):
#    List all Farms detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Season.objects.all()   
        serializer = SeasonSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Crop
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def cropdetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Crop.objects.all()   
        serializer = CropSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Well
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def welldetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Well.objects.all()   
        serializer = WellSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Yield
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def yielddetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Yield.objects.all()   
        serializer = YieldSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Member
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def memberdetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Member.objects.all()   
        serializer = MemberSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)

#View method for model Storage
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def storagedetail(request):
#    List all crops detail.
    if request.method == 'GET':
        #data = JSONParser().parse(request)
        data = Storage.objects.all()   
        serializer = StorageSerializer(data,many=True)
        t = JsonResponse(serializer.data, status=201,safe=False)
        t['Access-Control-Allow-Origin']='*'
        return t
    else:
        return JsonResponse(serializer.errors, status=400)