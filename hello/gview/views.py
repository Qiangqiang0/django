from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views import View

# Create your views here.

# 1) gview in app
class secondView(View):
    def get(self,request):
        u = reverse_lazy("gview:cats")
        u2 = reverse_lazy("gview:dogs")
        x = {"x1": u, "x2":u2}
        return render(request,"route/index.html",x)