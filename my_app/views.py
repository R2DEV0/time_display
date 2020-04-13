from django.shortcuts import render
from time import localtime, strftime

def date_time(request):
    context = {
        "time": strftime("%H:%M %p %Y-%m-%d", localtime())
    }
    return render(request,'index.html', context)
