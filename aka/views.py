from  django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def count(request):
    data =request.GET['fulltextarea']
    word_list = data.split()
    length = len(word_list)
    dict = {}
    for w in word_list:
        if w in dict:
            dict[w]+=1
        else:
            dict[w]=1
    dict_list = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)
    return render(request, 'count.html', {'d':data, 'l':length, 'dit':dict_list})
