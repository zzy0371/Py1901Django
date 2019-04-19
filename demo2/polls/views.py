from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Choices
# Create your views here.

def index(request):
    # return HttpResponse("首页")
    questions = Question.objects.all()
    return render(request,'polls/index.html',{"questions":questions})

def detail(request,id):
    question = Question.objects.get(pk=id)
    return render(request,'polls/detail.html',{"question":question})

def vote(request):
    id = request.POST["votenum"]
    choice = Choices.objects.get(pk=id)
    choice.votes += 1
    choice.save()
    # return HttpResponse("投票完成")
    return render(request,'polls/result.html',{"question":choice.question})