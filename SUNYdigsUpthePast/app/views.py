#root views

from django.shortcuts import render,get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Word
from .forms import *
from data import *

data = getOrderedElements()

#Controls Routing for the Home Page
def home(request):
    """Renders the home page."""
    id = 0
    id = int(request.GET.get('id', '0'))
    try:
        result = data[id]
    except:
        try:
            result = data[0]
        except:
            # WE SHOULD NEVER GET HERE UNLESS THE DATABASE HAS NOT BEEN POPULATED WITH DATA
            # OR FILE SYSTEM HAS BEEN MESSED WITH AND SOMETHING WENT WRONG
            print 'data'
            return render(request,"app/word.html")

    if request.method =="POST":
        form = TranslationForm(data=request.POST)
        if form.is_valid():
            if "submit" in request.POST:
                opinion = request.POST["submit"]
                #opinion = str(form.cleaned_data["submit"])
                print form.cleaned_data
                # DIG IT BUTTON
                if opinion.lower() == "dig it":
                    #add 1 to value
                    updateElement(id, 1)
                    return HttpResponseRedirect( '?id='+str(id+1))
                    #return render(request,'app/index.html')
                    #return render(request,'app/index.html', {'id':id+1})
                # BURY IT BUTTON
                elif opinion.lower() == "bury it":
                    #add -1 to value
                    updateElement(id, -1)
                    if id-1<=0:
                        return HttpResponseRedirect('?id='+str(dbcount()-1))
                    return HttpResponseRedirect( '?id='+str(id-1))
                    #return render(request,'app/word.html')
                    #return render(request,'app/word.html',{'id':(id+1)})
        
        print request.POST
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

#################################################################################
## THESE NEXT TWO FUNCTIONS CAN BE USED BUT ARE NOT RECOMMENDED... 
## THEY ARE THE UNFORMATTED VERSIONS OF THE HOME() FUNCTION
#################################################################################
######### Very simple display of word with image... (Deprecated) #############
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

############# initial attempt at home() Posting layout.... (Deprecated) #############
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
    return render(request,'app/err.html')
