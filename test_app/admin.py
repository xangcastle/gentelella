# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from gentelella.admin import ModelAdmin, GentelellaSite
from django.contrib.auth import admin as auth_admin, models as auth_models


vendedores = GentelellaSite(name="vendedores")

bodega = GentelellaSite(name="bodega")

# interface de los vendedores
class user_admin(auth_admin.UserAdmin, ModelAdmin):
    pass

vendedores.register(Producto, ModelAdmin)
vendedores.register(auth_models.User, user_admin)


# intefae bodega


class producto_admin(ModelAdmin):
    list_display = ('nombre', 'descripcion')


bodega.register(Producto, producto_admin)

