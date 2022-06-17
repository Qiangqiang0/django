from . import views
from django.urls import path


app_name = "gview"

urlpatterns = [
    path("cat",views.secondView.as_view(),name = "cats"),
    path("dog",views.secondView.as_view(),name = "dogs"),
    path("second",views.secondView.as_view(),name = "second_view")
    ]