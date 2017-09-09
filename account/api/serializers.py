from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer,  ValidationError, SerializerMethodField
from account.models import User
from rest_framework import status, serializers
from rolepermissions.roles import assign_role

class UserRegistrationSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  "phone",
                  "password",
                  "role",
                   )

    def create(self, validated_data):

        user = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            phone = self.validated_data['phone'],
            role = self.validated_data['role']
        )
        # assign_role(user,role)
        user.set_password(validated_data['password'])
        user.save()
        assign_role(user,self.validated_data['role'])
        return user
            # below is the hint for AbstractBaseUser DRF generation
            #http://www.cloudypoint.com/Tutorials/discussion/django-solved-how-to-create-a-new-user-with-django-rest-framework-and-custom-user-model/
            # user = super(UserRegistrationSerializer, self).create(validated_data)
