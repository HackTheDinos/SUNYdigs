#root views

from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Word
from .forms import *
from data import *

data = getOrderedElements()

def home(request):
    """Renders the home page."""
    id = request.GET.get('id', '0')
    if int(id) > 0:
        id = int(id)
    else:
        id = 0
            #DANGER - assumes that there is at least one element in data...
    try:
        result = data[id]
    except:
        try:
            result = data[0]
        except:
            return "somehow.... there are no more items that are in need of validation"
    if request.method =="POST":
        form = TranslationForm(data=request.POST)
        print id
        if form.is_valid():
            if "submit" in request.POST:
                opinion = request.POST["submit"]
                #opinion = str(form.cleaned_data["submit"])
                if opinion.lower() == "dig it":
                    #add 1 to value
                    updateElement(id, 1)
                    return render(request,'app/err.html')
                elif opinion.lower() == "bury it":
                    #add -1 to value
                    updateElement(id, -1)
                    return render(request,'app/word.html')
        
        print request.POST
    #        updateElement
        return "ADKLJFALDKS"
    else: # GET REQUEST
        assert isinstance(request, HttpRequest)

        translation = result["word"][1]
        
        form = TranslationForm(initial={'translation':translation})
    
        #NOTE NULL TRANSLATIONS WILL NOT BE RETRIEVED
        return render(
            request,
            'app/index.html',
            {'word':result["word"][0],'parenturl':result["imgpage"],'form':form}
            )





def word(request):
    assert isinstance(request, HttpRequest)
    id = request.GET.get('id', '0')
    if int(id) > 0:
        id = int(id)
    else:
        id = 0
    #DANGER - assumes that there is at least one element in data...
    try:
        result = data[id]
    except:
        try:
            result = data[0]
        except:
            return "somehow.... there are no more items that are in need of validation"

    translation = result["word"][1]
    form = TranslationForm(initial={'translation':result["word"][1]})
    
    # NOTE NULL TRANSLATIONS WILL NOT BE RETRIEVED
    
    # dont need other parameters
    return render(request,'app/word.html', {'word':result["word"][0],'parent':result["imgpage"],
                                           'form':form}
                  )


#def word(request,word_id):
def words(request,word_id):
    """Renders the individual word page"""
    assert isinstance(request, HttpRequest)
    type = request.GET.get('type', 'no_type_query')
    try:
        word = get_object_or_404(Word, id=word_id)
        form = TranslationForm(initial={'translation':word.name})
        url = word.pic_url
        desc = word.name
        return render(
            request,
            'app/words.html',
            {'word':type, 'link':url, 'description':desc, 'form':form}
            )
    except:
        return render(request,'app/err.html')

def yum(request):
    return render(request,'app/word.html')
