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

def index(request):
    list_items = ""
    months = list(monthly_chalenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = F"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")