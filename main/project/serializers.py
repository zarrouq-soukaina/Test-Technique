from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from .models import *
#JWT
from rest_framework_jwt.settings import api_settings

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields =('IdClasse', 'IdNatureIdt', 'IdPays', 'IdPays', 'NatureClient', 'Etat', 'IdCategorieAvoir','RaisonSociale','Matricule')
#Registration
class ClientRegistrationSerializer(serializers.ModelSerializer):

    profile = ClientSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_Client(**validated_data)
        Client.objects.create(
            user=user,
			Matricule=profile_data['Matricule'],
            IdClasse=profile_data['IdClasse'],
            IdNatureIdt=profile_data['IdNatureIdt'],
            IdPays=profile_data['IdPays'],
            NatureClient=profile_data['NatureClient'],
            Etat=profile_data['Etat'],
			IdCategorieAvoir=profile_data['IdCategorieAvoir'],
			RaisonSociale=profile_data['RaisonSociale'],
			
        )
        return user
class ControlleurRegistrationSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        user = User.objects.create_controlleuruser(**validated_data)
        
        return user

class ClientAccountCreatorRegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        user = User.objects.create_ClientAccountCreatoruser(**validated_data)
        
        return user


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }


class ComptesEspeceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComptesEspece
        fields ='__all__'


class ImputationsEspecesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ImputationsEspeces
        fields ='__all__'


