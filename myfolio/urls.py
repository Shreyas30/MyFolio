"""myfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('admin/', admin.site.urls),
    path('resume/', include('resume.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('forum/', include('forum.urls')),
    path('signup/',views.signupUser, name="SignupUser"),
    path('login/',views.loginUser, name="LoginUser"),
    path('logout/',views.logoutUser, name="LogoutUser"),
    path('about/',views.about, name="About"),
    path('contact/',views.contact, name="Contact"),
]
urlpatterns += staticfiles_urlpatterns()
