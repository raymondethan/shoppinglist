from django.db import models

# Create your models here.

class ShoppingItem(models.Model):
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name

class ShoppingList(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    list_name = models.CharField(max_length=200, default="list")

    def __str__(self):
        return self.list_name

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

class ItemList(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    item_key = models.ForeignKey(ShoppingItem)
    list_key = models.ForeignKey(ShoppingList)
    user_key = models.ForeignKey(User)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "item key: " + str(self.item_key) + ", list key: " + str(self.list_key) + ", user key: " + str(self.user_key)

class UserList(models.Model):
    list_key = models.ForeignKey(ShoppingList)
    user_key = models.ForeignKey(User)

    def __str__(self):
        return "list key: " + str(self.list_key) + ", user key: " + str(self.user_key)