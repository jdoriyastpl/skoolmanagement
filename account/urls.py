from django.conf.urls import url,include
from django.contrib.auth import views as auth_view
from account import views



app_name = 'account'

urlpatterns =[

    url(r'^profile/(?P<username>\w+)/$', views.user_profile, name='user_profile'),
    url(r'^profile/(?P<username>\w+)/edit/$', views.user_profile_update, name='user_profile_update'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^reset_password/$', views.ResetPasswordRequestView.as_view(), name="reset_password"),
    url(r'^reset_password_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            views.PasswordResetConfirmView.as_view(),name='reset_password_confirm'
        ),
]
