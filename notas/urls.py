from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("Gestiones",views.GestionViewset)
router.register("Estudiantes",views.EstudianteViewset)
router.register("EstudianteGestS",views.EstudianteGestionViewset)

urlpatterns = [
    path("",views.index,name="index"),
    path("Gestion/",views.Gestion1,name="gestion"),
    path('Materialista/', views.MateriaCreateView.as_view(),name="vista_materia"),
    path("Estudiante/cantidad",views.Estudiante_count,name="Categoriacont"),
    path('',include(router.urls))
]

