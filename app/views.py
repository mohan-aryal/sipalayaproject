from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.
'''
Type of views
function based view
class based view --> alternative way to implement views in python

# advantage of class based view -->  code organized in related to http method get, post, etc.
# code reuse (mixin)

class base view:
Based class view --> Api banaune use hunxa
Genric view
'''

from django.views import View

def show(request):
    return HttpResponse('Hello world!')

class Myview(View):
    name = "sujan"
    def get(self, request):

        return HttpResponse(f"Hello Class World! {self.name}")

# inheritance(mixins)
class Child(Myview):
    def get(self, request):
        return HttpResponse(f"Hello this child class {self.name}")

# based class (base view)
class HomeView(View):
    def get(self, request):
        data = Student.objects.all()

        return render(request, 'home.html', {'data': data})
    
    def post(self, request):
        name = request.POST['name']
        age = request.POST['age']

        Student.objects.create(name=name, age=age)
        return redirect('home')
