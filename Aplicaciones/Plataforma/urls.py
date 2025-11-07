from django.urls import path
from . import views
urlpatterns=[
    path('',views.verlogin),
    path('registrarTurno/',views.registrarTurno),
    path('edicionTurno/<codigo>',views.edicionTurno),
    path('borrarTurno/<codigo>',views.borrarTurno),
    path('editarTurno/',views.editarTurno),
    path('loguearse/',views.loguearse)
    

]

