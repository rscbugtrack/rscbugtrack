from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from trackingapp.models import Bugtrack

# def rschome(request):
#     html = ' <div style="text-align:center;"> <p  style="color:red;"> Welcome to RSC group </p> <br> \
#             <h3> This site is under maintenance </h3> </div> '

#     return HttpResponse(html)

def rschome(request):
    allrequirements = Bugtrack.objects.all()
    context = {'allreq':allrequirements}

    return render(request, 'rscbody.html', context)
