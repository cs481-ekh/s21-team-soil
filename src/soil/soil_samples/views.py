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
from reportlab.lib import colors

from google.oauth2 import id_token
from google.auth.transport import requests

from MySQLdb import _mysql

from .models import soil_sample
from .serializers import *
from ..settings import DATABASES
from data_object import soil_object
from soil_analyzer import soil_analyzer

import json

#import rpy2
#from rpy2.rinterface import R_VERSION_BUILD

# MySQLdb reference: https://mysqlclient.readthedocs.io/user_guide.html
# ReportLab Reference: https://www.reportlab.com/docs/reportlab-userguide.pdf

@api_view(['POST'])
def get_report(request):

    # create an array representing the dataFile json attribute from the client request
    file_array = request.data['dataFile']
    
    # If the array is empty, use the manually input fields as input to data_object. Otherwise, use the contents
    # from the array.
    soil = None
    
    if not file_array: 
        soil = soil_object(request.data['dataFile'], request.data['liquidLimit'], request.data['plasticIndex'], request.data['clayPercent'], request.data['siltPercent'], request.data['sandPercent'], request.data['organicContent'], request.data['stabilize'], request.data['limeDose'], request.data['cementDose'], request.data['quantResult'], request.data['qualResult'])
    else:
        for sample in file_array:
            soil = soil_object(sample['dataFile'], sample['liquidLimit'], sample['plasticIndex'], sample['clayPercent'], sample['siltPercent'], sample['sandPercent'], sample['organicContent'], sample['stabilize'], sample['limeDose'], request.data['cementDose'], sample['quantResult'], sample['qualResult'])
            
    # create predictor object
    analyzer = soil_analyzer()

    results = {}
            
    if (request.data['qualResult'] == True):
        if request.data['limeDose'] == True:
            result = analyzer.lime_regression(soil)
            results["limeRegression"] = result
        if request.data['cementDose'] == True:
            result = analyzer.cement_regression(soil)
            results["cementRegression"] = result
    if(request.data['quantResult'] == True):
        if request.data['limeDose'] == True:
            result = analyzer.lime_classification(soil)
            results["limeClassification"] = result
        if request.data['cementDose'] == True:
            result = analyzer.cement_classification(soil)
            results["cementClassification"] = result
        
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
    ts = TableStyle([
        ('FONTSIZE', (0,0), (10,1), 8),
        ('BACKGROUND', (0,0), (10,0), colors.HexColor("#cccccc"))
    ])

    # Add the report title
    p1 = Paragraph("<b>Statistical Soil Stabilizer Report</b>", headerStyle)

    headers = ["LL", "PL", "Clay %", "Silt %", "Sand %", "O.C. %", "Stabilizer", "Lime Reg.", "Cement Reg.", "Lime Cl.", "Cement Cl."]
    data = [request.data['liquidLimit'], request.data['plasticIndex'], request.data['clayPercent'], request.data['siltPercent'], request.data['sandPercent'], request.data['organicContent'], request.data['stabilize'], round(results['limeRegression'],4), round(results['cementRegression'],4), round(results['limeClassification'],4), round(results['cementClassification'],4)]
    tableData = [headers,data]

    t1 = Table(tableData)

    t1.setStyle(ts)

    elements.append(p1)
    elements.append(t1)

    # build the pdf from the elements list
    pdf_template.build(elements)

    # ensure we start from the beginning of the buffer
    buffer.seek(0)
    # return the buffer as a file response
    return FileResponse(buffer, as_attachment=True, filename="Geo_Report.pdf", content_type="application/pdf", status=status.HTTP_200_OK)

@api_view(['POST'])
def authenticate_user(request):
    token = request.data
    dbinfo=DATABASES['default']
    db=_mysql.connect(host=dbinfo['HOST'], user=dbinfo['USER'], passwd=dbinfo['PASSWORD'], db="dev_box")
    try:
        # idinfo contains all of the information from the user being authenticated
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "91335092244-a8nui54bma999p0f0f61uklj8095v6cl.apps.googleusercontent.com")
        firstName=idinfo['given_name']
        lastName=idinfo['family_name']
        email=idinfo['email']
        check="""SELECT * FROM auth_user WHERE email = "{email}" """.format(email=email)
        db.query(check)
        qr=db.store_result()
        qr=qr.fetch_row(maxrows=0,how=1)
        if (len(qr) > 0):
            query="""UPDATE auth_user SET last_login = CURRENT_TIMESTAMP"""
            db.query(query)
        else:
            query="""INSERT INTO auth_user (first_name, last_name, email, last_login) VALUES ("{fn}", "{ln}", "{email}", CURRENT_TIMESTAMP)""".format(fn=firstName,ln=lastName,email=email)
            db.query(query)

        db.close()
        return Response(data=qr,status=status.HTTP_200_OK)
    except ValueError as e:
        # Invalid token
        db.close()
        return Response(data=str(e),status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        # Some other error - most likely related to the DB connection/execution
        db.close()
        return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_users(request):
    dbinfo=DATABASES['default']
    db=_mysql.connect(host=dbinfo['HOST'], user=dbinfo['USER'], passwd=dbinfo['PASSWORD'], db="dev_box")
    try:
        query="""SELECT first_name,last_name,email,last_login FROM auth_user ORDER BY last_login DESC"""
        db.query(query)
        qr=db.store_result()
        qr=qr.fetch_row(maxrows=0,how=1)
        db.close()
        return Response(data=qr,status=status.HTTP_200_OK)
    except Exception as e:
        # Some other error - most likely related to the DB connection/execution
        db.close()
        return Response(data=str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)