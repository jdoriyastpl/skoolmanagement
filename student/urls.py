from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from student import views

app_name = 'student'

urlpatterns =[
    url(r'^$',views.StudentListView.as_view(),name='student_list'),
    url(r'^new/$', views.StudentCreateView.as_view(), name='student_new'),
    url(r'^(?P<pk>\d+)/$',views.StudentDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.StudentUpdateView.as_view(), name='student_edit')
]
