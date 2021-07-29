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


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month number")

    redirect_month = months[month-1]

    # make a dynamic url name
    redirect_path = reverse("challenge_month",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(response, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This Month is Not Supported")
