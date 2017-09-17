# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

ESTADO_PRODUCTO = (
    (1, 'PENDIENTE'),
    (2, 'EN VERIFICACION'),
    (3, 'PUBLICADO'),
    (4, 'DESHABILITADO')
)

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio_proveedor = models.FloatField(default=0.0)
    precio_venta = models.FloatField(default=0.0)
    precio_anterior_venta = models.FloatField(default=0.0)
    existencia = models.FloatField(default=0.0, verbose_name="en stock")
    descripcion = models.CharField(max_length=500)
    caracteristicasTecnica = models.CharField(max_length=10000)
    imagen = models.ImageField(upload_to="productos", null=True, blank=True)
    # cropping = ImageRatioField('imagen', '300x300', allow_fullsize=True)
    modelo = models.CharField(max_length=200)
    estado = models.IntegerField(choices=ESTADO_PRODUCTO, default=1)
    fecha_creacion = models.DateField(auto_now_add=True, blank=True)
    plantilla = models.CharField(max_length=500, default='home/product2.html')
    especial = models.BooleanField(default=False)


class Master(models.Model):
    column1 = models.CharField(max_length=100)
    column2 = models.CharField(max_length=100)
    column3 = models.CharField(max_length=100)
    column4 = models.CharField(max_length=100)


class Details(models.Model):
    master = models.ForeignKey(Master)
    column1 = models.CharField(max_length=100)
    column2 = models.CharField(max_length=100)
    column3 = models.CharField(max_length=100)
    column4 = models.CharField(max_length=100)
