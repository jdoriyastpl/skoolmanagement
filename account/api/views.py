from account.api.serializers import UserRegistrationSerializer,UserProfileSerializer
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from account.models import User
from rest_framework.decorators import api_view, permission_classes
from account.permissions import IsAuthenticatedOrReadOnly

@permission_classes((IsAuthenticatedOrReadOnly, ))
class UserRegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

@permission_classes((IsAuthenticatedOrReadOnly, ))
class UserProfileAPIView(RetrieveUpdateDestroyAPIView):
    '''
    Used lookup_field for custom filter
    '''
    serializer_class = UserProfileSerializer
    lookup_field = 'username'
    queryset = User.objects.all()
