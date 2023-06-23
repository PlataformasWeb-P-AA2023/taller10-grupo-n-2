from django.contrib import admin

# Register your models here.
from ordenamiento.models import *

class ParroquiaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'numVivienda','numParques','numEdificios', 'parroquia')
    search_fields = ('nombre','numParques')

admin.site.register(Barrio, BarrioAdmin)    