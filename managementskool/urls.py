"""managementskool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from . import views
from account.views import login_view as init_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',views.IndexView.as_view(),name='home'),
    url(r'^$', init_view ,name='login'),
    url(r'api/account/',include('account.api.urls',namespace='api-account')),
    url(r'account/',include('account.urls',namespace='account')),
    url(r'^teacher/',include('teacher.urls',namespace='teacher')),
    url(r'^student/',include('student.urls',namespace='student')),
    url(r'^standard/',include('standard.urls',namespace='standard')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
