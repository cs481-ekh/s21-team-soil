from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Soil
from .serializers import *

import json

import rpy2
from rpy2.rinterface import R_VERSION_BUILD
from rpy2.rinterface import R_VERSION_BUILD

@api_view(['GET', 'POST'])
def soil_sample(request):

    #if request.method == 'GET':
        # data = Soil.objects.all()

        # serializer = SoilSerializer(data, context={'request': request}, many=True)

        # return Response(serializer.data)

        # To be implemented later
     #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        serializer = SoilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # parse request.data
            data = json.load(request.data)
            soil = Soil_Object(data['dataFile'], data['liquidLimit'], data['plasticIndex'], data['clayPercent'], data['siltPercent'], data['sandPercent'], data['organicContent'], data['limeCementStabilize'], data['limeCementDose'], data['quantResult'], data['qualResult'])
            
            #soil = Soil_Object(data.dataFile, data.liquidLimit, data.plasticIndex, data.clayPercent, data.siltPercent, data.sandPercent, data.organicContent, data.limeCementStabilize, data.limeCementDose, data.quantResult, data.qualResult)

            #soil = Soil_Object(dataFile, liquidLimit, plasticIndex, clayPercent, siltPercent, sandPercent, organicContent, limeCementStabilize, limeCementDose, quantResult, qualResult)
            return Response(request.data, status=status.HTTP_201_CREATED)
            #return Response(request """status=status.HTTP_201_CREATED""")
            
        return Response(request.data, status=status.HTTP_201_CREATED)

"""@api_view(['PUT', 'DELETE'])
def soils_detail(request, pk):
    try:
        soil = Soil.objects.get(pk=pk)
    except Soil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SoilSerializer(soil, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        soil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""