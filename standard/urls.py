from django.conf.urls import url,include
from standard import views

app_name = 'standard'

urlpatterns =[
    url(r'^$',views.StandardListView.as_view(),name='standard_list'),
    url(r'^new/$', views.StandardCreateView.as_view(), name='standard_new'),
    url(r'^(?P<pk>\d+)/$',views.StandardDetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.StandardUpdateView.as_view(), name='standard_edit')
]
