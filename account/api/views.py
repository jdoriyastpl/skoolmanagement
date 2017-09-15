from account.api.serializers import UserRegistrationSerializer,UserProfileSerializer
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from account.models import User
from rest_framework.decorators import api_view, permission_classes
from account.permissions import IsAuthenticatedOrReadOnly
import json
from django.contrib.auth import authenticate, login
from rest_framework import status, views
from rest_framework.response import Response


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



class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                serialized = UserRegistrationSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)
