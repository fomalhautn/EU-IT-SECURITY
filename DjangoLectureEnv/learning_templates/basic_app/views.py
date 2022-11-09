from django.shortcuts import render
from . import forms
from basic_app.models import User

# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

def signup(request):
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

    return render(request, 'basic_app/signup.html', {'form':form})
