from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import Message
import json


def home(request):
    return render(request, 'home.html', {})

def index(request):
    return render(request, 'index.html', {})

@login_required
def room(request, room_name): 
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })



