from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from teacher import views

app_name = 'teacher'

urlpatterns =[
    url(r'^$',views.TeacherListView.as_view(),name='teacher_list'),
    url(r'^new/$', views.TeacherCreateView.as_view(), name='teacher_new'),
    url(r'^(?P<pk>\d+)/$',views.TeacherDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.TeacherUpdateView.as_view(), name='teacher_edit')
]
