from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),

    # Subject
    # path('subject/<str:name>', views.subject, name='subject'),

    # Resource
    # path('subject/<str:name>/resource/<int:resourceid>', views.resource, name='resource'),
    

]