from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse


# dictionary of months and its advices
monthly_challenges = {
    "january":  "january",  
    "february":  "february",  
    "march":  "march",  
    "april":  "april",  
    "may":  "may",  
    "june":  "june",  
    "july":  "july",  
    "august":  "august",  
    "september":  "september",  
    "october":  "october",  
    "november":  "november",  
    "december":  "december",  
}

# Create your views here.
def monthly_challenge_by_number(request, month):
    if month>=1 and month<=12:
        return HttpResponse(month)
    else:
        return HttpResponseNotFound("Month Number is Not Supported")
    

def monthly_challenge(response, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This Month is Not Supported")
    
