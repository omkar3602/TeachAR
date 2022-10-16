from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Subject
# Create your views here.
def index(request):
    subjects = Subject.objects.all()

    context = {
        'subjects':subjects,
    }
    return render(request, 'mainapp/index.html', context)