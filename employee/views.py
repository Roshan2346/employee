from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def list_all(request):
    return render(request, 'list_all.html')
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    count = len(wordlist)

    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    return render(request, 'count.html', {'fulltext': fulltext, 'count': count, 'worddict': worddict.items()})