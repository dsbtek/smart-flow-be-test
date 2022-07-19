from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import KycSerializer
from .models import Kyc

@csrf_exempt
def kycs(request):
    '''
        List all Kycs
    '''
    if(request.method == 'GET'):
        kyc = Kyc.objects.all()
        serializer = KycSerializer(kyc, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = KycSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def kyc(request, pk):
    try:
        customer = Kyc.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = KycSerializer(customer, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        customer.delete() 
        return HttpResponse(status=204)
    

