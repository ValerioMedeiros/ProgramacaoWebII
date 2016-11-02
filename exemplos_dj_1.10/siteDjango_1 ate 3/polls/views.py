#from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Question

"""
def index(request):
    template = loader.get_template('polls/index.html')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', <br>'.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))
"""


def index(request):#forma mais enxuta
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
""" #Versao com try e except
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questao nao existe!")
    return render(request,'polls/detail.html',{ 'question': question})
"""

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response = "You'e looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s." % question_id)
