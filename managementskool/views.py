from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count,Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class IndexView(LoginRequiredMixin,TemplateView):
    login_url = 'login'
    template_name ='dashboard.html'

    # def get_context_data(self,*args, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['Enrolled_students'] = Students.objects.filter(user=self.request.user).count()
    #     context['Pending_students'] = SendNotification.objects.filter(is_payment_pending=True).filter(user=self.request.user).count()
    #     return context
