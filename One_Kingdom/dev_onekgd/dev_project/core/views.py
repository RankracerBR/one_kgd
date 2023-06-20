from django.shortcuts import render
import pytz
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponseServerError

# Create your views here.

def index(request):
    context = {'timezone': str(timezone.get_current_timezone())}
    return render(request, 'index.html', context)
    
def form(request):
    pass
