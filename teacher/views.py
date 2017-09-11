from django.shortcuts import render
from teacher.forms import TeacherForm
from teacher.models import Teacher
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
class TeacherCreateView(LoginRequiredMixin,CreateView):
    template_name = 'teacher/form.html'
    login_url ='login'
    form_class = TeacherForm
    redirect_field_name = 'teacher/teacher_list.html'
    model = Teacher

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TeacherCreateView,self).form_valid(form)

class TeacherDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'teacher_detail'
    login_url = 'login'
    model = Teacher
    template_name = 'teacher/profile.html'

class TeacherUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    redirect_field_name = 'teacher/teacher_list.html'
    form_class = TeacherForm
    redirect_field_name = 'teacher/teacher_detail.html'
    model = Teacher
    template_name = 'teacher/form.html'

    # def get_form_kwargs(self):
    #         kwargs = super(TeacherUpdateView, self).get_form_kwargs()
    #         kwargs['user'] = self.request.user
    #         return kwargs

class TeacherListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Teacher
    paginate_by = 18
    def get_queryset(self):
        return Teacher.objects.filter(created_date__lte=timezone.now()).filter(user = self.request.user).order_by('-created_date')
