import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dictionary = {}

    for word in word_list:
        word = word.lower()
        symbols = "!@#$%^&*()_+<>?\":,./;[]-='"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
    word_dictionary = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',
                  {'fulltext': fulltext, 'count': len(word_list), 'word_dictionary': word_dictionary})

