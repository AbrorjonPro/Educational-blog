from .models import Contact
from django.shortcuts import render

def notifications(request):
    return ({'messages':Contact.objects.filter(status=False)})
