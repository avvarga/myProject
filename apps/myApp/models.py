from __future__ import unicode_literals

from django.db import models
import bcrypt
# Create your models here.
class UserManager (models.Manager):
    def valid_registration (self,postData):
        errors = []
        name = postData['name']
        username = postData['username']
        password = postData['password']
        pwd_confirm = postData['pwd_confirm']

        if len(name) ==0  :
            errors.append ("Your name is required")
        elif len(name) < 3:
            errors.append ("Your name should be at least 3 characters long")
        if len(username) == 0:
            errors.append ("Your username is required")
        elif len(username) < 3:
            errors.append ("Your username should be at least 3 characters long")
        if len(password) == 0:
            errors.append ("Your password is required")
        elif len(password) < 8:
            errors.append ("Your Password must be at least 8 characters long")
        if User.objects.filter(username = username):
            errors.append ('This username is already in use. Please log in instead.')
        if password != pwd_confirm:
            errors.append ('The password and password confirmation must match')
        return errors

    def valid_login (self,postData):
        errors =[]
        username = postData['username']
        password = postData['password']
        if len(username) == 0:
            errors.append ("Your username is required")
        elif len(username) < 3:
            errors.append ("Your username should be at least 3 characters long")
        if len(password) == 0:
            errors.append ("Please enter your password")
        try:
            user = User.objects.get(username = username)
            if bcrypt.checkpw ( password.encode(), user.password.encode() ):
                return errors
            errors.append ("Invalid username/password combination")
        except User.DoesNotExist:
            errors.append ("Invalid username/password combination")
        return errors

class ItemManager (models.Manager):
    def valid_item (self,postData):
        errors = []
        item = postData['item']
        if len(item) == 0:
            errors.append ("Please enter an item")
        elif len(item) < 3:
            errors.append ("The item's name must be at least 3 characters long")
        return errors

class User (models.Model):
    name = models.CharField (max_length = 255)
    username = models.CharField (max_length = 255)
    password = models.CharField (max_length = 255)
    objects = UserManager()    

    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.name


class Item (models.Model):
    name = models.CharField (max_length = 255)
    user = models.ForeignKey (User, related_name = 'user_items')
    wishlist = models.ManyToManyField (User, related_name = 'wish_items')     
    objects = ItemManager()

    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)

    def __str__(self):
        return self.name


