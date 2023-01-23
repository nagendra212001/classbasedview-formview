from django.shortcuts import render
from django.views.generic import FormView,ListView
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=NameForm

    def form_valid(self, form):
        return HttpResponse(str(form.cleaned_data))

class cbv_modelform(FormView):
    template_name='cbv_modelform.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data inserted successfully')

class Student_list(ListView):
    template_name='Student_list.html'
    model=Student
    #queryset=Student.objects.filter(name='nagendra')
    context_object_name='students'
    ordering=['name']

