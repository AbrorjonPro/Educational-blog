
from django.shortcuts import render
from django.conf import settings

def error_404_view(request, exception):
    data = {}
    return render(request,'404.html')

def error_500_view(exception):
    return render(exception, template_name='500.html')

def my_site_url(request):
    return {
        'SITE_URL': settings.SITE_URL,
    }