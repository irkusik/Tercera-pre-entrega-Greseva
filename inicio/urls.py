from django.urls import path
from inicio import views


urlpatterns = [
    path ('',views.inicio),
    path ('prueba/',views.prueba),
    path ('segunda-vista/',views.segunda_vista),
    path ('fecha-actual/',views.fecha_actual),
    path ('saludar/',views.saludar),
    path ('bienvenida/<str:nombre>/', views.bienvenida),
    path ('crear-tiburon/<str:tipo>/<str:habitat>/<int:tomaño>/<str:status>/', views.crear_tiburon),
    path ('crear-ballena/<str:tipo>/<str:habitat>/<int:tomaño>/<str:status>/', views.crear_ballena), 
    path ('crear-animal/<str:nombre>/<str:orden>/<str:habitat>/<int:tomaño>/', views.crear_animal)   
]