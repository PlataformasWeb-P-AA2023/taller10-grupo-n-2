from django.db import models

# Create your models here.


class Parroquia(models.Model):
    opciones_tipo_Parroquia = (
        ('urbano', 'Urbano'),
        ('rural', 'Rural'),
    )

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length = 30,\
        choices = opciones_tipo_Parroquia)
    
    def __str__(self):
        return "%s - %s" % (self.nombre, self.tipo)


class Barrio(models.Model):
    opciones_Parques = (
        ('uno', '1'),
        ('dos', '2'),
        ('tres', '3'),
        ('cuatro', '4'),
        ('cinco', '5'),
        ('seis', '6'),
    )

    nombre = models.CharField(max_length=30)
    numVivienda = models.IntegerField()
    numParques = models.CharField(max_length = 30, \
                choices = opciones_Parques)
    numEdificios = models.IntegerField()
    
    parroquia = models.ForeignKey(Parroquia, related_name = 'los_barrios',
                on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s - %d - %s - %d" % (self.nombre, self.numVivienda, self.numParques, self.numEdificios)