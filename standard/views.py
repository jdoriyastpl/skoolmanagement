from django.shortcuts import render
from standard.forms import StandardForm
from standard.models import Standard
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.
class StandardCreateView(LoginRequiredMixin,CreateView):
    template_name = 'standard/form.html'
    login_url ='login'
    form_class = StandardForm
    redirect_field_name = 'standard/standard_list.html'
    model = Standard

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(StandardCreateView,self).form_valid(form)

class StandardDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'standard_detail'
    login_url = 'login'
    model = Standard
    template_name = 'standard/standard_detail.html'

class StandardUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    redirect_field_name = 'standard/standard_list.html'
    form_class = StandardForm
    redirect_field_name = 'standard/standard_detail.html'
    model = Standard
    template_name = 'standard/form.html'

    # def get_form_kwargs(self):
    #         kwargs = super(TeacherUpdateView, self).get_form_kwargs()
    #         kwargs['user'] = self.request.user
    #         return kwargs

class StandardListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Standard
    paginate_by = 18
    def get_queryset(self):
        return Standard.objects.all()
