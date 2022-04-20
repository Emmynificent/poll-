from django.urls import path
from . import views

urlpatterns=[
    path('', views.hello),
    path('vote', views.vote),
    path('details/<int:question_id>', views.details)
    
]