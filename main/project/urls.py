from django.urls import path

from . import views
from .views import *



urlpatterns = [
    path('signup/controlleur/',ControlleurRegistrationView.as_view(),name='signup_controlleur'),
	path('signup/ClientAccountCreator/',ClientAccountCreatorRegistrationView.as_view(),name='signup_ClientAccountCreator'),
    path('AddClientAccount/',ClientRegistrationView.as_view(),name='signup_client'),
    path('signin/',UserLoginView.as_view()),
    path('profile/',UserProfileView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('client-list/',ClientList.as_view(), name="client-list"),
    path('get_delete_update_client/<str:pk>/', views.RetrieveUpdateDestroytClientAPIView.as_view(), name='get_delete_update_client'),
    path('get_delete_update_compte/<str:pk>/', views.RetrieveUpdateDestroytComptesEspeceAPIView.as_view(), name='get_delete_update_compte'),
    path('ComptesEspeceList/', ComptesEspeceList.as_view(), name="ComptesEspeceList"),
    path('ComptesEspeceCreate/', views.ComptesEspeceCreateView.as_view(), name="ComptesEspeceCreate"),


    path('ImputationsEspecesList/', views.ImputationsEspecesList.as_view(), name="ImputationsEspecesListt"),
    
    path('ImputationsEspecesCreate/', views.ImputationsEspecesCreateView.as_view(), name="ImputationsEspecesCreate"),
   path('get_delete_update_ImputationsEspeces/<str:pk>/', views.RetrieveUpdateDestroytImputationsEspecesAPIView.as_view(), name='get_delete_update_ImputationsEspeces'),


	

]