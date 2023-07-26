from django.db import models
class Developer(models.Model):
    codigo_empleado=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    OPCIONES_AREA=(
        ('desarrollo','Desarrollo'),
        ('diseno','Diseño'),
        ('ventas','Ventas')
    )
    area=models.CharField(
        max_length=20,
        choices=OPCIONES_AREA,
        default='desarrollo'
    )

class Mascota(models.Model):
    nombre=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to='mascotas/')
    nombre_corto=models.CharField(max_length=30,unique=True)
    duenho=models.ForeignKey(Developer,on_delete=models.CASCADE)

class Juguete(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=3,decimal_places=2)
    url=models.URLField()
    creador=models.ForeignKey(Developer, on_delete=models.CASCADE)

class Juguete_Mascota(models.Model):
    juguete=models.ForeignKey(Juguete,on_delete=models.CASCADE)
    mascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)