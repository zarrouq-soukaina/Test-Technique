from rest_framework.permissions import BasePermission



class IsClientUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)


class IsClientUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)


class IsControllerUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_controlleur)
        
class IsClientAccountCreatorUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_clientAccountCreator)