from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Documentation

def doc_list(requests):
    docs = Documentation.objects.all()
    context = {
    'docs': docs,
    'last_release': docs[len(docs)-1],
    }
    return render(requests, 'index.html', context=context)

def doc(requests, version):
    context = {
        'document':get_object_or_404(Documentation, version=version)
    }
    return render(requests, 'document.html', context=context)
