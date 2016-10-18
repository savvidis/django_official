from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('polls.views',
url(r'^$', 'index', name='index'),
)
