from django.urls import path
from inicio import views



urlpatterns = [
    path ('',views.inicio, name='inicio'),
    #path ('prueba/',views.prueba, name='prueba'),
    #path ('segunda-vista/',views.segunda_vista, name='segunda_vista'),
    #path ('fecha-actual/',views.fecha_actual, name='fecha_actual'),
    #path ('saludar/',views.saludar, name='saludar'),
    #path ('bienvenida/<str:nombre>/', views.bienvenida, name='bienvenida'),
    # V1 crear
    #path ('crear-tiburon/<str:tipo>/<str:habitat>/<int:tomaño>/<str:status>/', views.crear_tiburon, name='crear_tiburon'),
    #path ('crear-ballena/<str:tipo>/<str:habitat>/<int:tomaño>/<str:status>/', views.crear_ballena, name='crear_ballena'), 
    #path ('crear-animal/<str:nombre>/<str:orden>/<str:habitat>/<int:tomaño>/', views.crear_animal, name='crear_animal')   
    ## V2 crear
    path ('tiburones/crear/', views.crear_tiburon, name='crear_tiburon'),
    path ('tiburones/', views.listar_tiburones, name='listar_tiburones'),
    path ('ballenas/crear/', views.crear_ballena, name='crear_ballena'), 
    path ('ballenas/', views.listar_ballenas, name='listar_ballenas'),
    path ('animales/crear/', views.crear_animal, name='crear_animal'),
    path ('animales/', views.listar_animales, name='listar_animales'),   
]