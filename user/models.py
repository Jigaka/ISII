from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def getIdUsuario(self):
        return self.id

    def getNombreUsuario(self):
        return self.username

    def getNombre(self):
        return self.first_name

    def getApellido(self):
        return self.last_name

    def getEmail(self):
        return self.email