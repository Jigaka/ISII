from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.shortcuts import redirect
from django.contrib import messages
from allauth.account.models import EmailAddress
from allauth.account.utils import user_email, user_field, user_username
from allauth.utils import valid_email_or_none
from login.models import ListaPermitidos



class RestrictEmailAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request,sociallogin):
        """
        Para permitir registrarse por google
        """
        return True


    def pre_social_login(self, request, sociallogin):
        """
        Esta funcion controla que los usuarios a registrase o loguearse
        fueron ingresados previamente por el administrador
        """

        lista = ListaPermitidos.objects.all()
        lista_permitida = [element.correo for element in lista]
        try:
            email = sociallogin.account.extra_data['email'].lower()

        except EmailAddress.DoesNotExist:
            return
        if email not in lista_permitida:
            messages.add_message(request, messages.ERROR, 'Contacte al admistrador para que te cree una cuenta')
            raise ImmediateHttpResponse(redirect('/'))

    def populate_user(self, request, sociallogin, data):
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        name = data.get("name")
        user = sociallogin.user
        user_username(user, username or "")
        user_email(user, valid_email_or_none(email) or "")
        name_parts = (name or "").partition(" ")
        user_field(user, "first_name", first_name or name_parts[0])
        user_field(user, "last_name", last_name or name_parts[2])
        print(user)
        return user


class RestrictEmailAdapterAccount(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        """
        Este proyecto no permitira registrase por medio de correo
        y contraseña
        """
        return False
