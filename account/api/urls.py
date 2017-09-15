from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from account.api.views import UserRegistrationAPIView,LoginView

app_name = 'api-account'

urlpatterns =[
     url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/register/$', UserRegistrationAPIView.as_view(), name='register'),

]
