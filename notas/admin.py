from django.contrib import admin
from .models import Gestion, Estudiante, Materia,Curso,Estudiante_Gestion,Curso_Materia,notas


# Register your models here.
#gestion
class GestionAdmin(admin.ModelAdmin):
    list_display=('sem','anio')
    list_filter=('sem','anio')
    search_fields=('anio','anio')
    ordering=('sem','anio')
admin.site.register(Gestion,GestionAdmin)
#Estudiante
class EstudianteAdmin(admin.ModelAdmin):
    list_display=('ci','nombre','firstname','Lastname','fone','address')
    list_filter=('ci','nombre','firstname')
    search_fields=('ci','ci')
    ordering=('ci','nombre','firstname','Lastname','fone','address')
admin.site.register(Estudiante,EstudianteAdmin)
#Materia
class MateriaAdmin(admin.ModelAdmin):
    list_display=('nombre','tipo')
    list_filter=('nombre','tipo')
    search_fields=('nombre','nombre')
admin.site.register(Materia,MateriaAdmin)
#curso
class CursoAdmin(admin.ModelAdmin):
    list_display=('nombre','tipo')
    list_filter=('nombre','tipo')
    search_fields=('nombre','nombre')
admin.site.register(Curso,CursoAdmin)
#Estudiante_Gestion
class Estudiante_Gestion_Admin(admin.ModelAdmin):
    list_display=('estudiante_id','gestion_id')
    list_filter=('estudiante_id','gestion_id')
    search_fields=('estudiante_id','gestion_id')
admin.site.register(Estudiante_Gestion,Estudiante_Gestion_Admin)
#Curso_materia
class Curso_Materia_Admin(admin.ModelAdmin):
    list_display=('curso_id','materia_id')
    list_filter=('curso_id','materia_id')
    search_fields=('curso_id','materia_id')
admin.site.register(Curso_Materia,Curso_Materia_Admin)
class Notas_Admin(admin.ModelAdmin):
    list_display=('valor','tipo','curs_mat_id','est_gest_id')
    list_filter=('valor','tipo','curs_mat_id','est_gest_id')
    search_fields=('valor','tipo','curs_mat_id','est_gest_id')
admin.site.register(notas,Notas_Admin)