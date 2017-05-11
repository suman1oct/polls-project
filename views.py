from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice 
from django.template import loader
from django.shortcuts import render,get_object_or_404 
from django.urls import reverse
from .models import Choice,Question
from django.views import generic
from django.utils import timezone


def detail(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def result(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	return render(request,'polls/result.html',{'question':question})
def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question,'error_message':"you didn't select a choice.",})
	else:
		selected_choice.votes+=1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))"""


class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='Latest_question_List'

	def get_queryset(self):
		"""Return the last five published question(not including those set to be published in the future)"""
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'
	def get_queryset(self):
		"""Exclude any question that aren't published yet"""
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'

def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question':question,'error_message':"you didn't select a choice.",})
	else:
		selected_choice.votes+=1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


