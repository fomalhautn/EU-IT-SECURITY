from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
def index(request):
    return HttpResponse("<em>My Second App</em>")
'''

def hello(request):
    return HttpResponse('Hello! You just success to run URLs mmapping. Conrgs!')

def index(request):
    my_dict = {'insert_me': "Hello, i am from views.py !"}
    return render(request, 'second_app/index.html', context=my_dict)