from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, SimpleDocTemplate
from reportlab.platypus.tables import Table, TableStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import ParagraphStyle

from google.oauth2 import id_token
from google.auth.transport import requests


from .models import soil_sample
from .serializers import *

import json

#import rpy2
#from rpy2.rinterface import R_VERSION_BUILD

@api_view(['GET', 'POST'])
def insert_soil_sample(request):

    #if request.method == 'GET':
        # data = Soil.objects.all()

        # serializer = SoilSerializer(data, context={'request': request}, many=True)

        # return Response(serializer.data)

        # To be implemented later
     #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        serializer = soilserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # parse request.data
            data = json.load(request.data)
            
            soil = soil_object(data['dataFile'], data['liquidLimit'], data['plasticIndex'], data['clayPercent'], data['siltPercent'], data['sandPercent'], data['organicContent'], data['limeCementStabilize'], data['limeCementDose'], data['quantResult'], data['qualResult'])
            
            # # create predictor object
            analyzer = soil_analyzer()

            # # Assume lime classificaton analysis for now.
            # result = predict.compute_lime_classification(soil)


            # Choose an analysis to run based on json fields
            if("quantResult" == False):
                if "limeDose" == True:
                    result = analyzer.lime_classification(soil)
                else: 
                    result = analyzer.cement_classification(soil)
            else:
                if "limeDose" == True:
                    result = analyzer.lime_regression(soil)
                else: 
                    result = analyzer.cement_regression(soil)

            # Return the results somehow
            # print(result)

            return Response(result, status=status.HTTP_200_OK)
            #return Response(request """status=status.HTTP_201_CREATED""")
            
        return Response(request, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def authenticate_user(request):
    token = request.data
    try:
        # idinfo contains all of the information from the user being authenticated
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "91335092244-a8nui54bma999p0f0f61uklj8095v6cl.apps.googleusercontent.com")
        return Response(idinfo,status=status.HTTP_200_OK)
    except ValueError as e:
        # Invalid token
        return Response(data=str(e),status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def report(request):
    
    buffer = BytesIO()

    pdf_template = SimpleDocTemplate(buffer,
                                     rightMargin=72,
                                     leftMargin=72,
                                     topMargin=72, 
                                     bottomMargin=72,
                                     # Uncomment the following line to show the page margins on the PDF.
                                     #showBoundary=1,
                                     pageSize=letter
                                     )

    # container for pdf elements
    elements = []

    headerStyle = ParagraphStyle('HEADER', alignment=1, fontSize=16, spaceAfter=16)

    # Add the 
    p1 = Paragraph("<b>Statistical Soil Stabilizer Report</b>", headerStyle)

    # Uncomment the following lines to see some examples of default paragraph/tables
    #p2 = Paragraph("Lorem ipsum")
    #t1 = Table([(1,2),(3,4)])

    elements.append(p1)
    #elements.append(p2)
    #elements.append(t1)

    # build the pdf from the elements list
    pdf_template.build(elements)

    # ensure we start from the beginning of the buffer
    buffer.seek(0)
    # return the buffer as a file response
    return FileResponse(buffer, as_attachment=True, filename="Geo_Report.pdf", content_type="application/pdf", status=status.HTTP_200_OK)

#@api_view(['PUT', 'DELETE'])
#def soils_detail(request, pk):
#    try:
#        soil = Soil.objects.get(pk=pk)
#    except Soil.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method == 'PUT':
#        serializer = SoilSerializer(soil, data=request.data,context={'request': request})
#        if serializer.is_valid():
#            serializer.save()
#            return Response(status=status.HTTP_204_NO_CONTENT)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    elif request.method == 'DELETE':
#        soil.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)