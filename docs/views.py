from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Documentation

def doc_list(requests):
    docs = Documentation.objects.all()
    if docs:
        context = {
        'docs': docs,
        'last_release': docs[len(docs)-1],
        }
    else:
        context = {'docs':None}

    return render(requests, 'docs/index.html', context=context)

def doc(requests, lang):
    context = {
        'document':get_object_or_404(Documentation, language=lang)
    }
    return render(requests, 'docs/document.html', context=context)
