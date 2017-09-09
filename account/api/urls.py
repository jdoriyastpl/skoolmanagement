from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from account.api.views import UserRegistrationAPIView

app_name = 'api-account'

urlpatterns =[

    url(r'^register/$', UserRegistrationAPIView.as_view(), name='register'),
    
]
