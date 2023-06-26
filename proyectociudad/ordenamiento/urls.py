"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('parroquia/barrios', views.mostrar_Parroquias_Barrios, 
            name='mostrar_Parroquias_Barrios'),
        path('crear/parroquia', views.crear_parroquia, 
            name='crear_parroquia'),
        path('editar_parroquia/<int:id>', views.editar_parroquia, 
            name='editar_parroquia'),
        # numeros telefonicos
        path('barrios/<int:id>', views.obtener_Barrios, 
            name='obtener_Barrios'),
        path('barrios/', views.mostrar_Barrios, 
            name='mostrar_Barrios'),
        path('editar_barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
        path('crear/barrio/parroquia/<int:id>', 
            views.crear_barrio_parroquia, 
            name='crear_barrio_parroquia'),
]