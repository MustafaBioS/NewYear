from django.shortcuts import render
import datetime

# Create your views here.


def isitnewyear(request):   
    now = datetime.datetime.now()
    return render(request, "isitnewyear/newyear.html", {
        "newyear": now.month == 1 and now.day == 1,
        "newyeareve": now.month == 12 and now.day == 31
    })
