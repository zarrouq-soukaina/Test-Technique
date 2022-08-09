from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
	
	def create_user(self, email, password=None):
		"""
		Create and return a `User` with an email, username and password.
		"""
		if not email:
			raise ValueError('Users Must Have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

    
	def create_superuser(self, email, password):
		"""
		Create and return a `User` with superuser (admin) permissions.
		"""
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user
        

	def create_controlleuruser(self,email,password):
		if password is None:
			raise TypeError('controlleur must have a password')
		user = self.create_user(email,password)
		user.is_controlleur = True
		user.save()
		return user

    
	def create_ClientAccountCreatoruser(self,email,password):
		if password is None:
			raise TypeError('Client Account Creators must have a password')
		user = self.create_user(email,password)
		user.is_clientAccountCreator = True
		user.save()
		return user

	def create_Client(self,email,password):
		if password is None:
			raise TypeError('Client  must have a password')
		user = self.create_user(email,password)
		user.is_client = True
		user.save()
		return user


    
    
  
		
class User(AbstractBaseUser):

	
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_clientAccountCreator = models.BooleanField(default=False)
	is_controlleur = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	
	objects = UserManager()

	def __str__(self):
		return self.email
	class Meta:
		db_table = "login"

class Client (models.Model):  
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    IdClasse = models.IntegerField(null=True)
    IdNatureIdt = models.IntegerField(null=True)
    IdPays = models.IntegerField(null=True)
    NatureClient = models.CharField(max_length=100, null=True)
    Etat = models.CharField(max_length=100, null=True)
    IdCategorieAvoir = models.IntegerField(null=True)
    RaisonSociale = models.CharField(max_length=100, null=True)
    Matricule = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.user.email
    
class ComptesEspece (models.Model):
    
    IdClient  = models.ForeignKey(Client, on_delete=models.CASCADE)
    IdDepositaire = models.IntegerField(null=True)
    DateCreation = models.DateField(default=datetime.now)
    Web = models.CharField(max_length=100, null=True)
    Etat = models.CharField(max_length=100, null=True)
   
class ImputationsEspeces (models.Model):
    
    IdCompteEspece = models.ForeignKey(ComptesEspece, on_delete=models.CASCADE)
    Sens = models.IntegerField(null=True)
    Montant= models.IntegerField(null=True)
    DateImputation = models.DateField(max_length=30, null=True)
    IdSDBCompte= models.IntegerField(null=True)
    NatureClient = models.CharField(max_length=100, null=True)
    DateValeur = models.DateField(max_length=30, null=True)
    Etat = models.CharField(max_length=100, null=True)
    IdDateValeur= models.IntegerField(null=True)
    Nature = models.CharField(max_length=100, null=True)
    DateEtat = models.DateField(max_length=30, null=True)
    libelle = models.CharField(max_length=100, null=True)
    


    
