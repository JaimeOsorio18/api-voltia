from django.db import models

class Equipo(models.Model):
    equipo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

class Mantenimiento(models.Model):
    mantenimiento_id = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)

class Lectura(models.Model):
    lectura_id = models.AutoField(primary_key=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha = models.DateField()
    valor = models.CharField(max_length=100)
