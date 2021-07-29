from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        month_path = reverse("challenge_month", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>" 
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month number")

    redirect_month = months[month-1]

    # make a dynamic url name
    redirect_path = reverse("challenge_month", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(response, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f"<h1>{challenge_text}</h1>")
    except:
        return HttpResponseNotFound("<strong>This Month is Not Supported</strong>")
