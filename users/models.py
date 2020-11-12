"""Users app models"""

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Manages user mapped objects"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError(
                _('Los usuarios deben tener una dirección de correo electrónico.')
            )
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name, last_name):
        """Creates and saves a new superuser"""
        user = self.create_user(
            email, password,
            first_name=first_name, last_name=last_name
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Default user for project."""
    email = models.EmailField(
        _('correo electrónico'),
        unique=True,
        error_messages={
            'unique': _("Un usuario con ese correo ya existe."),
        },
    )
    first_name = models.CharField(_('nombre(s)'), max_length=150)
    last_name = models.CharField(_('apellido(s)'), max_length=150)
    is_staff = models.BooleanField(
        _('¿Es staff?'),
        default=False,
        help_text=_(
            'Designa si el usuario puede iniciar sesión en este sitio de administración.'
        ),
    )
    is_active = models.BooleanField(
        _('¿Está activo?'),
        default=True,
        help_text=_(
            'Designa si este usuario debe tratarse como activo. '
            'Deseleccione esto en lugar de eliminar cuentas.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('fecha de registro'),
        auto_now_add=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('usuario')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name
