from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer,  ValidationError, SerializerMethodField
from account.models import User
from rest_framework import status, serializers
from rolepermissions.roles import assign_role
from django.contrib.auth import update_session_auth_hash

class UserRegistrationSerializer(ModelSerializer):
    confirm_password = validated_data.get('confirm_password', None)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "username",
                  "email",
                  "phone",
                  "password",
                  "confirm_password",
                  "role",
                   )

    def create(self, validated_data):
        '''
        # below is the hint for AbstractBaseUser DRF generation
        #http://www.cloudypoint.com/Tutorials/discussion/django-solved-how-to-create-a-new-user-with-django-rest-framework-and-custom-user-model/
        # user = super(UserRegistrationSerializer, self).create(validated_data)
        '''
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

class UserProfileSerializer(ModelSerializer):
    '''
    default details serializers
    '''
    class Meta:
        model = User
        fields = ("first_name",
                  "last_name",
                  "email",
                  "phone",
                  "picture",
                  "school",
                  "address")

    def update(self,instance, validated_data):
        instance.phone = validated_data.get('phone',instance.phone)
        instance.school = validated_data.get('school',instance.school)
        instance.picture = validated_data.get('picture',instance.picture)

        instance.save()

        password = validated_data.get('password',None)
        if password:
            instance.set_password(password)
            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)
        return instance
