#root views

from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Word

def home(request):
    """Renders the home page."""
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



def word(request,word_id):
    """Renders the individual word page"""
    #print "alskdfjalkdsjfads"
    assert isinstance(request, HttpRequest)
    try:
        word = get_object_or_404(Word, id=word_id)
        url = word.pic_url
        
        return render(
            request,
            'app/word.html',{'word':"adskfjlka;djflkadsjf", 'link':url}
            )
    except:
        return render(request,'app/err.html')

