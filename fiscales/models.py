from django.db import models

# Create your models here.

class Fiscales(models.Model):
    nombre_sucursal = models.CharField(max_length=60)
    numero_sucursal = models.CharField(max_length=5)
    modelo_fiscal = models.CharField(max_length=40)
    vencimiento_certificado_digital = models.DateField(blank=True,null=True)
    punto_venta = models.IntegerField()
    numero_serie = models.IntegerField()
    fecha_cambio = models.DateField()
    estado = models.CharField(max_length=100)


class Historial(models.Model):
    nombre_sucursal = models.CharField(max_length=60)
    numero_sucursal = models.CharField(max_length=5)
    modelo_fiscal = models.CharField(max_length=40)
    vencimiento_certificado_digital = models.DateField(blank=True,null=True)
    punto_venta = models.IntegerField()
    numero_serie = models.IntegerField()
    fecha_cambio = models.DateField()
    estado = models.CharField(max_length=100)
    fecha_modificacion = models.DateField(auto_now=True)