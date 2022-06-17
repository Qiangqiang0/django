"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

# app_name = "gview"

urlpatterns = [
    path('admin/', admin.site.urls),

    # pre-defined class from django
    #path("",TemplateView.as_view(template_name = 'views/main.html'))

    # function from 
    path('funky',views.funky),
    path('danger',views.danger),
    path("rest/<int:guess>",views.rest),
    # class
    path('main',views.MainView.as_view()),
    path("remain/<slug:guess>",views.RemainView.as_view()),
    path('tmpl/<int:guess>',views.GameView.as_view()),
    path('tmplb/<int:guess>',views.GameView2.as_view()),
    # givew from app
    path("gview123/",include("gview.urls",namespace = "gview_test")),
    path("forms/",include("forms.urls"))


]
