from django.shortcuts import render
from django.http import HttpResponse

from papp.models import Question
# Create your views here.
def hello(request):
    return HttpResponse('hello there!')

def vote(request):
    return HttpResponse('Vote here')

def details(request, question_id):
    pass



