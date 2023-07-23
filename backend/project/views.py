from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from .models import *
from datetime import datetime
from django.contrib.auth.models import User
from .forms import *

# Create your views here.

# binary search algorithm
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return False

def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            timestamp = datetime.now()
            # input from user by form
            input_value_str = request.POST["input_value"]
            # convert to list of integers
            input_value = [int(x.strip()) for x in input_value_str.split(",")]
            # reverse sort the list
            input_value.sort(reverse=True)
            search = int(request.POST["search"])
            # apply binary search on the list and find the targeted value
            result = binary_search(input_value, search)
            # save the data in the database
            data = Data(input_value=input_value, timestamp=timestamp, user=request.user)
            data.save()

            return JsonResponse({'result': result})
        return render(request, "project/index.html")
    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "project/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "project/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "project/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "project/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "project/register.html")