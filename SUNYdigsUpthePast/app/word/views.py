#HOME VIEW

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import get_object_or_404


def wordsindex(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
                'title':'Index Page',
            'year':datetime.now().year,
        })
    )

def word(request):
    assert isinstance(request, HttpRequest)
    return render(request,'app/err.html')

def words(request,word_id):
    """Renders the individual word page"""
    print "alskdfjalkdsjfads"
    assert isinstance(request, HttpRequest)
    word = get_object_or_404(Word, id=word_id)
    return render(
        request,
        'app/word.html',{'word':"adskfjlka;djflkadsjf", 'link':'dummylinkf4now.net'}
    )

