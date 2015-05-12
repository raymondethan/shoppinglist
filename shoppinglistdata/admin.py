from django.contrib import admin

# Register your models here.
from .models import ShoppingItem, ShoppingList, User, ItemList, UserList

admin.site.register(ShoppingItem)
admin.site.register(ShoppingList)
admin.site.register(User)
admin.site.register(ItemList)
admin.site.register(UserList)