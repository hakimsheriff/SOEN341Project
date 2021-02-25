"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from pigeonpost import views as core_views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name = 'login.html'), name='login'),
    url(r'^logout$', LogoutView.as_view(),  name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),


]
