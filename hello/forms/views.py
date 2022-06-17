from django.shortcuts import render
from django.views import View
# Create your views here.

class formsView(View):
    def get(self,request):
        return render(request,"forms/main.html")


# 2) csrf
class csrfExample(View):
    def get(request):
        response = """<html>
        <body>
        <form method="POST">
            <p> <label for = "guess"> Input Guess </label>
            <input type = "text" name = "guess" size = '40' id = "guess"/> </p> 
        </form>
        </body>
        </html>"""
