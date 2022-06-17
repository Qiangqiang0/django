from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class firstGview(View):
    def get(self,request):
        return render(request, "gview/gview.html")

class route(View):
    def get(self,request):
        response = '''
        <body>
        <p> This is example!</p>''' + '''
        <p> This is guess </p>
        </body>
        '''
        return render(request,'gview/main.html')



