from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from AppTwo.models import User
from AppTwo.forms import NewUserForm

def index(request):
    return render(request, 'second_app/index.html')

def users(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'second_app/users.html', {'form':form})

#from AppTwo.models import AccessRecord, Topic, Webpage, User

'''
def index(request):
    return HttpResponse("<em>My Second App</em>")

def hello(request):
    return HttpResponse('Hello! You just success to run URLs mmapping. Conrgs!')

def index(request):
    #my_dict = {'insert_me': "Hello, i am from views.py !"}
    #return render(request, 'second_app/index.html', context=my_dict)
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'second_app/index.html', context=date_dict)
    #return render(request, 'second_app/index.html', {'data': AccessRecord.objects.all})

def index2(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'second_app/index2.html', context=date_dict)
    #return render(request, 'second_app/index.html', {'data': AccessRecord.objects.all})
'''
