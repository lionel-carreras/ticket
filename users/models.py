from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD

class CustomUser(AbstractUser):
    sucursal = models.ForeignKey(
       'soporte.Sucursal',
        verbose_name= "Sucursal",
=======
from django.db import models

class CustomUser(AbstractUser):
    sucursal = models.ForeignKey(
        'soporte.Sucursal',
        verbose_name="Sucursal",
>>>>>>> 7e7119f6153acca9634f8a5ef8d11d5ad665ff81
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column='sucursalid_usuario',
    )
<<<<<<< HEAD
    must_change_password = models.BooleanField(
        default=True,
        help_text="Si es True, el usuario debe cambiar la contraseña en su próximo inicio de sesión."
    )
=======
>>>>>>> 7e7119f6153acca9634f8a5ef8d11d5ad665ff81
