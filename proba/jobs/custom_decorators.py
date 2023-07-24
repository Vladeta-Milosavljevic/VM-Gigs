import functools
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from django.http import HttpResponseRedirect
from .models import Job


def authentication_not_required(view_func, redirect_url="jobs:index"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        messages.warning(request, "You need to be logged out")
        print("You need to be logged out")
        return redirect(redirect_url)
    return wrapper


def creator_only(function):
    @wraps(function)
    def wrap(request, pk):
        job = Job.objects.get(pk=pk)
        user_id = request.user.id if request.user.id else 0
        if user_id == job.user_id:
            return function(request, pk)
        else:
            messages.success(request, "You do not have the required permision.",
                             extra_tags='alert-danger')
            return HttpResponseRedirect('/')

    return wrap


def creator_and_super_user_only(function):
    @wraps(function)
    def wrap(request, pk):
        job = Job.objects.get(pk=pk)
        user_id = request.user.id if request.user.id else 0
        if user_id == job.user_id or request.user.is_superuser:
            return function(request, pk)
        else:
            messages.success(request, "You do not have the required permision.",
                             extra_tags='alert-danger')
            return HttpResponseRedirect('/')

    return wrap


def super_user_only(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        super_user = request.user.is_superuser if request.user else 0
        if super_user:
            return function(request)
        else:
            messages.success(request, "You do not have the required permision.",
                             extra_tags='alert-danger')
            return HttpResponseRedirect('/')

    return wrap
