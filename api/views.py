from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def householddetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Household.objects.filter(HID=request.POST["HID"])   
        serializer = HouseholdSerializer(data,many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def farmdetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Farm.objects.filter(FID=request.POST["HID"])   
        serializer = FarmSerializer(data,many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def welldetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Well.objects.filter(WID=request.POST["HID"])   
        serializer = WellSerializer(data,many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def memberdetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Member.objects.filter(MID=request.POST["HID"])   
        serializer = MemberSerializer(data,many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def cropdetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Crop.objects.filter(FID=request.POST["HID"])   
        serializer = CropSerializer(data,many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def yielddetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = Yield.objects.filter(WID=request.POST["HID"]) 
        serializer = YieldSerializer(data,many=True)
        return JsonResponse(serializer.data, status=201,safe=False)
    else:
        return JsonResponse(serializer.errors, status=400)
    
@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def housedetail(request,dat_id):
    data = {}
    household = Household.objects.filter(HID=dat_id)
    household = HouseholdSerializer(household,many=True)
    data["Household"]=household.data
    member = MemberSerializer(Member.objects.filter(HID=dat_id),many=True)
    data["Member"]=member.data
    well = WellSerializer(Well.objects.filter(HID=dat_id),many=True)
    temp = well.data
    for i in range(len(temp)):
        k = temp[i]["WID"]
        ser = YieldSerializer(Yield.objects.filter(WID=k),many=True)
        temp[i]["Yield"] = ser.data
    data["Well"] = temp
    temp = FarmSerializer(Farm.objects.filter(HID=dat_id),many=True)
    temp = temp.data
    for i in range(len(temp)):
        k = temp[i]["FID"]
        ser = CropSerializer(Crop.objects.filter(FID=k),many=True)
        temp[i]["Crop"] = ser.data
    data["Farm"] = temp
    return JsonResponse(data, status=201,safe=False)

@detail_route(renderer_classes=(renderers.StaticHTMLRenderer,))
@csrf_exempt
def HouseholdALL(request):
    data = {}
    household = Household.objects.all()
    household = HouseholdSerializer(household,many=True)
    temp = household.data
    for i in range(len(temp)):
        data[i] = {}
        home = HouseholdSerializer(Household.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Household"] = home.data
        member = MemberSerializer(Member.objects.filter(HID=temp[i]["HID"]),many=True)
        data[i]["Member"] = member.data
        well = WellSerializer(Well.objects.filter(HID=temp[i]["HID"]),many=True)
        temp2 = well.data
        for j in range(len(temp2)):
            k = temp2[j]["WID"]
            ser = YieldSerializer(Yield.objects.filter(WID=k),many=True)
            temp2[j]["Yield"] = ser.data
        data[i]["Well"] = temp2
        farm = FarmSerializer(Farm.objects.filter(HID=temp[i]["HID"]),many=True)
        temp2 = farm.data
        for j in range(len(temp2)):
            k = temp2[j]["FID"]
            ser = CropSerializer(Crop.objects.filter(FID=k),many=True)
            temp2[j]["Crop"] = ser.data
        data[i]["Farm"] = temp2
    return JsonResponse(data, status=201,safe=False)