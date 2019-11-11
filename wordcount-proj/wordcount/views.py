from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse('Hello')
    #return render(request,'home.html',{'title':'A test of python dictionary from view to html file'})
    return render(request,'home.html')

def rice(request):
    #return HttpResponse('I like Rice and stew for launch')
    return HttpResponse('<h1>I like Rice and stew for launch<h1/>')

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            wordDictionary[word] += 1 #Increase
        else:
            wordDictionary[word] = 1 #add to word dictionary

    return render(request,'count.html',{'fulltextkey':fulltext,'count':len(wordlist),'wordDictionary':wordDictionary})