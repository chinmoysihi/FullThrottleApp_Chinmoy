from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from datetime import datetime

dateFormat =  '%b %d %Y %I:%M%p'

# From Models import User Defined Models
from .models import Employee,ActivityPeriods
# Create your views here.

def index(request):
    return HttpResponse("<h1><em>To get API details enter /getEmployee in the url.</em></h1>")

def getEmployees(request):
    response_Dictionary = dict()

    Employees = Employee.objects.all()

    if(Employees):

        # Set response "ok" filed as True
        response_Dictionary['ok'] = 'true'

        for employee in Employees:

            employee_user = Employee.objects.get(id = employee.id)
            activityP = []
            for period in ActivityPeriods.objects.filter(Employee__exact = employee):
                t1 = period.start_time
                t2 = period.end_time

                activityP.append({
                'start_time': datetime.strftime(t1,dateFormat),
                'end_time': datetime.strftime(t2,dateFormat)
                })

            #if members not present in dictionary add the members
            if 'members' not in response_Dictionary:
                response_Dictionary['members'] = list()

            #Add all Employee Data from Database in JSON
            response_Dictionary['members'].append({
                'id':employee.id,
                'real_name':employee.real_name,
                'tz':str(employee.tz),
                'activity_periods':activityP
            })
    else:
        # Set 'ok' as false when no employees are present
        response_Dictionary['ok'] = 'false'
    # print(response_Dictionary)
    return JsonResponse(response_Dictionary,safe=False)
