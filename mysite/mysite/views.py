from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages



def home(request):
    return render(request, 'home.html', {})
    
def home_copy(request):
    return render(request, 'home_copy.html', {})