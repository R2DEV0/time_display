from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def random(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    random_context = {
        'a_string': get_random_string(length=14),
        'count': request.session['counter']
    }
    return render(request,'index2.html', random_context)


def generate(request):
    return redirect('/generate')


def reset_count(request):
    request.session['counter'] = 0
    return redirect('/random')
