from django.shortcuts import render
from django.contrib import messages
from utils.decorator import login_required_message
from django.contrib.auth.decorators import login_required


from .models import Subject, Topic
# Create your views here.
def index(request):
    subjects = Subject.objects.all()

    context = {
        'subjects':subjects,
    }
    return render(request, 'mainapp/index.html', context)

@login_required_message(message="Please log in, in order to view the requested page.")
@login_required
def subject(request, name):
    subject = Subject.objects.get(name=name)

    topics = Topic.objects.filter(subject=subject)
    
    context = {
        'subject':subject,
        'topics':topics,
    }

    return render(request, 'mainapp/subject/subject.html', context)