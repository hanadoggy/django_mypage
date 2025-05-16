from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_chalenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 mintues every day!",
    "march": "Learn Django for at least 30 mintues every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 mintues every day!",
    "june": "Learn Django for at least 30 mintues every day!",
    "july": "Eat no meat for the entire month!",
    "auguest": "Walk for at least 20 mintues every day!",
    "september": "Learn Django for at least 30 mintues every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 mintues every day!",
    "december": "Learn Django for at least 30 mintues every day!"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_chalenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # challenges/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_chalenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")