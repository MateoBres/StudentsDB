"""Fichero views."""
#Django
from django.http import HttpResponse
#utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting and date"""
    return HttpResponse('Hello World! Now is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))