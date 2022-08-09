from django.shortcuts import render

# to build API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .models import *
from .serializers import *
# to Use the token to retrieve profiles
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.views import APIView
from .permissions import *
from django.db import connection
#CRUD d'un Client

#Voir fichier permissions.py 
#Permission est pour les controlleurs et l'admin qui est un superuser 
class ClientList(generics.ListAPIView):
	permission_classes = [IsAuthenticated&IsControllerUser]
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

#Permission est pour les controlleur
#requete SQL
#Select DISTINCT c.*
#from Clients c
#INNER JOIN ComptesEspece e
#on e.IdClient=c.IdPersonne
#INner join SummarisedAmounts ac
#on ac.idcompteespece = e.idcompte
#Where ac.mnt > X * (
#select Avg(mnt) from SummarisedAmounts
#where ac.idcompteespece=idcompteespece
#and julianday(YearMonth) - julianday('DateEtat') BETWEEN 30 AND 36*30
#);  
#Pour l'exemple X = 2 et  Date : exemple '01-09-2005’
class ClientSuspectList(generics.ListAPIView):
	permission_classes = [IsAuthenticated&IsControllerUser]
	
	serializer_class = ClientSerializer
	queryset = Client.objects.raw('Select DISTINCT c. from Clients c INNER JOIN ComptesEspece e on e.IdClient=c.IdPersonne INner join SummarisedAmounts ac on ac.idcompteespece = e.idcompte Where ac.mnt > X * ( select Avg(mnt) from SummarisedAmounts where ac.idcompteespece=idcompteespece and julianday(YearMonth) - julianday(DateEtat) BETWEEN 30 AND 36*30')

	

#Permission est pour les controlleurs
class RetrieveUpdateDestroytClientAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer
   
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated&IsControllerUser]

#CRUD d'un ComptEspece
class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)

#Permission est pour les Createur de ComptClient

class ComptesEspeceList(generics.ListAPIView):
	permission_classes = [IsAuthenticated&IsClientAccountCreatorUser]
	queryset = ComptesEspece.objects.all()
	serializer_class = ComptesEspeceSerializer
#Permission est pour les Createur de ComptClient
class RetrieveUpdateDestroytComptesEspeceAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComptesEspeceSerializer
   
    queryset = ComptesEspece.objects.all()
    permission_classes = [IsAuthenticated&IsClientAccountCreatorUser]

#Permission est pour les Createur de ComptClient 
class ComptesEspeceCreateView(CreateAPIView):

    serializer_class = ComptesEspeceSerializer
    permission_classes = [IsAuthenticated&IsClientAccountCreatorUser]
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Comptes Especes created  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    
#CRUD d'un Transaction


class ImputationsEspecesList(generics.ListAPIView):
	permission_classes = [IsAuthenticated&IsClientAccountCreatorUser]
	queryset = ImputationsEspeces.objects.all()
	serializer_class = ImputationsEspecesSerializer




class ImputationsEspecesCreateView(CreateAPIView):

    serializer_class = ImputationsEspecesSerializer
    permission_classes = [IsAuthenticated&IsClientAccountCreatorUser]
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Imputations Especes created  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class RetrieveUpdateDestroytImputationsEspecesAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImputationsEspecesSerializer
   
    queryset = ImputationsEspeces.objects.all()
    permission_classes = [IsAuthenticated&IsClientAccountCreatorUser]

#Registration 

class ControlleurRegistrationView(CreateAPIView):

    serializer_class = ControlleurRegistrationSerializer
    permission_classes = (AllowAny,)
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Controlleur registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class ClientAccountCreatorRegistrationView(CreateAPIView):

    serializer_class = ClientAccountCreatorRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'ClientAccountCreator registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

class ClientRegistrationView(CreateAPIView):

    serializer_class = ClientRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Client registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

#Profiles
class UserProfileView(RetrieveAPIView):
	permission_classes = (AllowAny,)
	authentication_class = JWTAuthentication

	def get(self, request):
		try:
			if request.is_controlleur== True:
				user_profile = User.objects.get(id=request.id)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'controlleur fetched successfully',
					'data': [{
						'email': user_profile.email,
						
					}]
				}
			if request.is_clientAccountCreator == True:
				user_profile = User.objects.get(id = request.id)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'clientAccountCreator profile fetched successfully',
					'data': [{
						'email': user_profile.email,
						}]
				}
			if request.user.is_superuser == True:
				userprofile = User.objects.get(user = request.id)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'Admin profile fetched successfully',
					'data': [{
						'email': user_profile.email,
					}]
				}
			
			if request.user.is_client == True:
				user_profile = Client.objects.get(user=request.user)
				status_code = status.HTTP_200_OK
				response = {
					'success': 'true',
					'status code': status_code,
					'message': 'client profile fetched successfully',
					'data': [{
						'IdClasse': user_profile.IdClasse,
					
					}]
				}

		except Exception as e:
			status_code = status.HTTP_400_BAD_REQUEST
			response = {
				'success': 'false',
				'status code': status.HTTP_400_BAD_REQUEST,
				'message': 'User does not exists',
				'error': str(e)
				}
		return Response(response, status=status_code)



