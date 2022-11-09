from django.shortcuts import render
from . import forms

# Create your views here.
from django.http import HttpResponse

from basicapp.models import User
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.Formname()

    if request.method == 'POST':
        form = forms.Formname(request.POST)

        if form.is_valid():
            # do something
            form_name = form.cleaned_data['name']
            form_email = form.cleaned_data['email']
            form_text = form.cleaned_data['text']
            u = User(name=form_name, email=form_email, text=form_text)
            u.save()

    return render(request, 'basicapp/signup.html', {'form':form})

