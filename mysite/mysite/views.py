from django.shortcuts import render, redirect, get_object_or_404
from custom_user.models import Item
from django.core.urlresolvers import reverse
from django.contrib import messages



def home(request):
    item = Item.objects.get(pk=1)
    #print item
    return render(request, 'home.html', {'item':item})
    
def home_copy(request):
    return render(request, 'home_copy.html', {})