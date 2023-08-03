from django.http import HttpResponse
from django.shortcuts import render
from app.forms import *
from django.views.generic import FormView
from django.http import HttpResponse

# Create your views here.
class form_class(FormView):
    template_name = 'form_class.html'
    form_class = StudentForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('Data has been saved')


