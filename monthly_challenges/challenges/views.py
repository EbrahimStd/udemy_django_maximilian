from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def monthly_challenge_by_number(request, month):
    if month>=1 and month<=12:
        return HttpResponse(month)
    else:
        return HttpResponseNotFound("Month Number is Not Supported")
    

def monthly_challenge(response, month):
    challenge_text = None
    if month == "january":
        challenge_text = "January"
    elif month == "february":
        challenge_text = "February"
    elif month == "march":
        challenge_text = "March"
    else:
        return HttpResponseNotFound("This Month is Not Supported")

    return HttpResponse(challenge_text)
