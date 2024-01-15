#!/usr/bin/env python3
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice


def index(request):
    """this is the view for the root route"""
    try:
        last_5_questions = Question.objects.order_by('-pub_date')[:5]
    except Question.DoesNotExist:
        raise Http404("the question(s) do(es) not exist")
    index_template = loader.get_template("polls/index.html")
    index_ctx = {"last_5_questions": last_5_questions}
    # output = ("  ,".join([x.question_text for x in last_5_questions]))
    return HttpResponse(index_template.render(index_ctx, request))


def detail(request, question_id=""):
    """this is the view for the /polls/[SLUG] endpoint"""
    try:
        question = Question.objects.get(id=question_id)
        detail_template = loader.get_template("polls/details.html")
        detail_ctx = {"question": question}
        return HttpResponse(detail_template.render(detail_ctx, request))
    except Http404:
        raise Http404("question not found")


def results(request, question_id=""):
    """this is the view for the /polls/[SLUG]results/ endpoint"""
    try:
        question = Question.objects.get(pk=question_id)
        result_template = loader.get_template("polls/results.html")
        result_ctx = {"question": question}
        return HttpResponse(result_template.render(result_ctx, request))
    except Question.DoesNotExist:
        raise Http404("This is not a valid question")


def vote(request, question_id=""):
    """this is the view for the /polls/vote/[SLUG] endpoint"""
    try:
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("this is not a valid question")
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        raise Http404("you didn't select a valid choice")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))
