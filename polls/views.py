from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Question, Choise
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def home(request):
    return HttpResponse('Home')

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.POST)
    try:
        selected_choise= question.choise_set.get(pk=request.POST['choise'])
    except (KeyError, Choise.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':'You didnt select a choice',
        })
    else:
        selected_choise.votes +=1
        selected_choise.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

