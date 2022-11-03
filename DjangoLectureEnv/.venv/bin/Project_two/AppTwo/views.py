from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from AppTwo.models import AccessRecord, Topic, Webpage, User

'''
def index(request):
    return HttpResponse("<em>My Second App</em>")
'''

def hello(request):
    return HttpResponse('Hello! You just success to run URLs mmapping. Conrgs!')

'''
def index(request):
    #my_dict = {'insert_me': "Hello, i am from views.py !"}
    #return render(request, 'second_app/index.html', context=my_dict)
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'second_app/index.html', context=date_dict)
    #return render(request, 'second_app/index.html', {'data': AccessRecord.objects.all})
'''
def index2(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'second_app/index2.html', context=date_dict)
    #return render(request, 'second_app/index.html', {'data': AccessRecord.objects.all})

