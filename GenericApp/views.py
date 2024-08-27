from django.shortcuts import render
from .models import Detail
from .form import DetailForm
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView


# Create your views here.

'''
Generic class-based views
high level of abstraction which is used for rapid development.
# built in views:
    TemplateView: Displays a static HTML template.
    ListView: Displays a list of objects.
    DetailView: Displays a single object.
    CreateView: Allows adding new objects.
    UpdateView: Allows updating existing objects.
    DeleteView: Allows deleting objects.
'''

class IndexView(ListView):
    model = Detail
    template_name = 'index.html'
    context_object_name = 'data'

class CreateForm(CreateView):
    template_name = 'form.html'
    form_class = DetailForm
    model = Detail
    success_url = '/generic/'

class UpdateForm(UpdateView):
    template_name = 'update.html'
    model=Detail
    fields='__all__'
    success_url = '/generic/'

class DeleteForm(DeleteView):
    model = Detail
    success_url = '/generic/'




