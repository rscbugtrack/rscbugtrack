from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def rschome(request):
    html = ' <div style="text-align:center;"> <p  style="color:red;"> Welcome to RSC group </p> <br> \
            <h3> This site is under maintenance </h3> </div> '

    return HttpResponse(html)
