#!/usr/bin/env python3
# Create your views here.
from django.db.models import F
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    """the class representation of the index view"""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """returns the last five published questions"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """the class representation for the details view"""
    model = Question
    template_name = "polls/details.html"


class ResultsView(generic.DetailView):
    """the class representation for the results view"""
    model = Question
    template_name = "polls/results.html"


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
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        selected_choice.refresh_from_db()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))
