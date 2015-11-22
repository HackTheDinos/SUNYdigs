from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # /word/4/
                       url(r'^$', 'app.word.views.wordindex'),
                       url(r'^(?P<word_id>[0-9]+)/$', 'app.views.word', name='word'),

)
