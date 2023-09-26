from django.contrib.auth.models import Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleManager(models.Manager):
    """
    Default Django groups renames to Roles
    """
    use_in_migrations = False

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Role(models.Model):
    name = models.CharField(_('name'), max_length=150, unique=True)
    description = models.CharField(_("Description"), max_length=255, null=True, blank=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissions'),
        blank=True,
        db_table='users_roles_permissions',
        related_name='roles',
    )

    objects = RoleManager()

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
