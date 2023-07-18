from django.urls import path
from inicio import views



urlpatterns = [
    path ('',views.inicio, name='inicio'),
    path('contact/', views.contact, name='contact'), ###
    path('about/', views.about, name='about'), ####
    #path ('prueba/',views.prueba, name='prueba'),
    #path ('segunda-vista/',views.segunda_vista, name='segunda_vista'),
    #path ('fecha-actual/',views.fecha_actual, name='fecha_actual'),
    #path ('saludar/',views.saludar, name='saludar'),
    #path ('bienvenida/<str:nombre>/', views.bienvenida, name='bienvenida'),
    #vistas comunes
    # V1 crear
    #path ('crear-tiburon/<str:tipo>/<str:habitat>/<int:tomaño>/<str:status>/', views.crear_tiburon, name='crear_tiburon'),
    #path ('crear-ballena/<str:tipo>/<str:habitat>/<int:tomaño>/<str:status>/', views.crear_ballena, name='crear_ballena'), 
    #path ('crear-animal/<str:nombre>/<str:orden>/<str:habitat>/<int:tomaño>/', views.crear_animal, name='crear_animal')   
    ## V2 crear
   # path ('tiburones/', views.listar_tiburones, name='listar_tiburones'),
   # path ('tiburones/crear/', views.crear_tiburon, name='crear_tiburon'),
   # path ('tiburones/eliminar/<int:tiburon_id>', views.eliminar_tiburon, name='eliminar_tiburon'),
   # path ('tiburones/modificar/<int:tiburon_id>', views.modificar_tiburon, name='modificar_tiburon'),
   # path ('ballenas/', views.listar_ballenas, name='listar_ballenas'),
   # path ('ballenas/crear/', views.crear_ballena, name='crear_ballena'),
   # path ('ballenas/eliminar/<int:ballena_id>', views.eliminar_ballena, name='eliminar_ballena'), 
   # path ('ballenas/modificar/<int:ballena_id>', views.modificar_ballena, name='modificar_ballena'), 
   # path ('animales/', views.listar_animales, name='listar_animales'),
   # path ('animales/crear/', views.crear_animal, name='crear_animal'),
   # path ('animales/eliminar/<int:animal_id>', views.eliminar_animal, name='eliminar_animal'),
   # path ('animales/modificar/<int:animal_id>', views.modificar_animal, name='modificar_animal'), 

 # CBV
    
    path('tiburones/', views.ListarTiburones.as_view() , name='listar_tiburones'),
    path('tiburones/crear/', views.CrearTiburon.as_view() , name='crear_tiburon'),
    path('tiburones/eliminar/<int:pk>/',views.EliminarTiburon.as_view(), name='eliminar_tiburon'),
    path('tiburones/modificar/<int:pk>/',views.ModificarTiburon.as_view(), name='modificar_tiburon'),   
    path('tiburones/<int:pk>/',views.MostrarTiburon.as_view(), name='mostrar_tiburon'),   

    path('ballenas/', views.ListarBallenas.as_view() , name='listar_ballenas'),
    path('ballenas/crear/', views.CrearBallena.as_view() , name='crear_ballena'),
    path('ballenas/eliminar/<int:pk>/',views.EliminarBallena.as_view(), name='eliminar_ballena'),
    path('ballenas/modificar/<int:pk>/',views.ModificarBallena.as_view(), name='modificar_ballena'),   
    path('ballenas/<int:pk>/',views.MostrarBallena.as_view(), name='mostrar_ballena'),   

    path('animales/', views.ListarAnimales.as_view() , name='listar_animales'),
    path('animales/crear/', views.CrearAnimal.as_view() , name='crear_animal'),
    path('animales/eliminar/<int:pk>/',views.EliminarAnimal.as_view(), name='eliminar_animal'),
    path('animales/modificar/<int:pk>/',views.ModificarAnimal.as_view(), name='modificar_animal'),   
    path('animales/<int:pk>/',views.MostrarAnimal.as_view(), name='mostrar_animal'),   
]




