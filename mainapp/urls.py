from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # Subject
    path('subject/<str:name>', views.subject, name='subject'),
    
]