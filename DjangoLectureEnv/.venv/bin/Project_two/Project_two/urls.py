"""Project_two URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""
from django.conf.urls import url, include
from django.contrib import admin
from AppTwo import views

'''
urlpatterns = [
    url(r'^$', views.index2, name='index2'),
    url(r'^AppTwo', include('AppTwo.urls')),
    url(r'^admin', admin.site.urls)
]



urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^AppTwo', include('AppTwo.urls')),
    url(r'^admin', admin.site.urls)
]
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^formpage/', views.form_name_view, name='form_name'),
]
'''

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.users, name='users'),
]


'''
urlpatterns = [
    url(r'^AppTwo', include('AppTwo.urls')),
    url(r'^/admin', admin.site.urls),
]

from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


urlpatterns = [
    url(r'^$', views.index2, name='index2'),
]
'''