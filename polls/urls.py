from django.conf.urls import url, patterns
from . import views

app_name = 'polls'
urlpatterns = patterns('polls.views',
    url(r'^$', 'index', name='index') ,
    url(r'^(?P<question_id>[0-9])/$','detail', name="detail") ,
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
)
