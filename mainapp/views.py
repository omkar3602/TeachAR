from django.shortcuts import render, redirect
from django.contrib import messages
from utils.decorator import login_required_message
from django.contrib.auth.decorators import login_required


from .models import Subject, Topic
from utils.email_sender import send_mail
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

@login_required
def send_email(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        receiver_email = data['email']
        sender_name = data['sender_name']
        sender_email = data['sender_email']
        subject_name = data['subject_name']
        topic_name = data['topic_name']
        effect_link = data['effect_link']

        send_mail(receiver_email, sender_name, sender_email, subject_name, topic_name, effect_link)


        messages.info(request, f'Email sent to {receiver_email}')
        return redirect('subject', subject_name)
    return redirect('home')