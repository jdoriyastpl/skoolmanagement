from account.api.serializers import UserRegistrationSerializer,UserProfileSerializer
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from account.models import User



class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserProfileAPIView(RetrieveUpdateDestroyAPIView):
    '''
    Used lookup_field for custom filter
    '''
    serializer_class = UserProfileSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
