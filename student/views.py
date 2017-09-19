from django.shortcuts import render
from student.forms import StudentForm
from student.models import Student
from django.contrib import messages
from django.utils import timezone
from section.signals import update_count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (View,TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.
class StudentCreateView(LoginRequiredMixin,CreateView):
    template_name = 'student/form.html'
    login_url ='login'
    form_class = StudentForm
    redirect_field_name = 'student/student_list.html'
    model = Student

    def form_valid(self,form):
        print("ffsdfgddgdf")
        student_name = form.cleaned_data.get('name')
        student_standard = form.cleaned_data.get('standard')
        student_section = form.cleaned_data.get('section')
        print(student_name)
        update_count.send(sender = Student, name =student_name, standard = student_standard,section =student_section)
        return super(StudentCreateView,self).form_valid(form)




class StudentDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'student_detail'
    login_url = 'login'
    model = Student
    template_name = 'student/profile.html'

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'login'
    redirect_field_name = 'student/student_list.html'
    form_class = StudentForm
    redirect_field_name = 'student/student_detail.html'
    model = Student
    template_name = 'student/form.html'

    # def get_form_kwargs(self):
    #         kwargs = super(TeacherUpdateView, self).get_form_kwargs()
    #         kwargs['user'] = self.request.user
    #         return kwargs

class StudentListView(LoginRequiredMixin,ListView):
    login_url = 'login'
    model = Student
    paginate_by = 18
    def get_queryset(self):
        return Student.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
