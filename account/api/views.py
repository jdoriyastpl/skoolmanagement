from account.api.serializers import UserRegistrationSerializer
from rest_framework.generics import CreateAPIView
from account.models import User



class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
