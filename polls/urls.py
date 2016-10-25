from django.conf.urls import url, patterns
from . import views

app_name = 'polls'
urlpatterns = patterns('polls.views',
    url(r'^$', views.IndexView.as_view(), name='index') ,
    url(r'^(?P<pk>[0-9])/$', views.DetailView.as_view(), name="detail") ,
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', 'vote', name='vote'),
)
