from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin,Permission,_user_get_all_permissions,_user_has_perm,_user_has_module_perms
# from myauth import PermissionsMixin,Permission,_user_get_all_permissions,_user_has_perm,_user_has_module_perms
# Create your models here.


from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from myauth import AbstractBaseUser, BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import Group




# class GroupProfile(models.Model):
#     group = models.OneToOneField(Group, unique=True)
#     a = models.CharField(max_length=100)
#     b = models.CharField(max_length=100)


Group.add_to_class('url', models.CharField(max_length=100))
Group.add_to_class('detail', models.CharField(max_length=100))

# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user







class MyUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(
        verbose_name='username ',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True

        return super(MyUser, self).has_perm(perm,obj=obj)
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        # print perm
        # print self.groups.permissions,111111111111111
        # # print self.user_permissions,11111111

        # return _user_has_perm(self, perm, obj)

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    # @property
    # def is_superuser(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin


class Host(models.Model):
    server_name = models.CharField(max_length=64)

    class Meta:
        permissions = (
            ('access_dashboard', u'access_dashboard'),
            ('access_log', u'access_log'),
            ('access_role_manage', u'access_role_manage'),
            ('access_user_manage', u'access_user_manage'),
        )