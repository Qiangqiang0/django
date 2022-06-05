from django.views import View
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.html import escape


# 1 funky 
def funky(request):
    response = '''
    <body>
    <p> This is example!</p>
    </body>
    '''
    return(HttpResponse(response))

# 2. funky
def danger(request):
    response = '''
    <body>
    <p> This is example!</p>''' + request.GET['guess']+ '''
    <p> This is guess </p>
    </body>
    '''
    return(HttpResponse(response))

# 3. escape
def rest(request,guess):
    response = '''
    <body>
    <p> This is example!</p>''' + escape(guess)+ '''
    <p> This is guess </p>
    </body>
    '''
    return(HttpResponse(response))

# 4. calss 
class MainView(View):
    def get(self,request):
        response = '''
        <body>
        <p> This is example!</p>''' + '''
        <p> This is guess </p>
        </body>
        '''
        return(HttpResponse(response))

# 5) class new 
class RemainView(View):
    def get(self,request,guess):
        response = '''
        <body> <p> your guess is ''' + escape(guess)+ \
        '''</p></body>
        '''
        return(HttpResponse(response))