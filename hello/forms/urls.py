from django.urls import path
from . import views

urlpatterns = [
    path("forms",views.formsView.as_view())

]