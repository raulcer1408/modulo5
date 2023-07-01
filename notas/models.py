from django.db import models
from .validators import validate_sem,validate_sem_len,validate_anio_len
from django.core.validators import RegexValidator,validate_unicode_slug
# Create your models here.

class Gestion(models.Model):
    sem=models.CharField(max_length=50,validators=[validate_sem,validate_sem_len])
    anio=models.CharField(max_length=50,validators=[validate_anio_len])
   
    def __str__(self):
       return self.anio
    
class Estudiante(models.Model):
    ci=models.CharField(max_length=50,primary_key=True)
    nombre=models.CharField(max_length=200,validators=[
       RegexValidator(
          regex='^[a-zA-Z]*$',
          message=('El nombre solo debe contener letras ')
       )
    ])
    firstname=models.CharField(max_length=200,validators=[
       RegexValidator(
          regex='^[a-zA-Z]*$',
          message=('El apellido paterno solo debe contener letras ')
       )
    ])
    Lastname=models.CharField(max_length=200,validators=[
       RegexValidator(
          regex='^[a-zA-Z]*$',
          message=('El apellido materno solo debe contener letras ')
       )
    ])
    fone=models.CharField(max_length=50,validators=[
       RegexValidator(
          regex='^[0-9]*$',
          message=('El telefono solo debe contener numeros ')
       )
    ])
    address=models.CharField(max_length=200,validators=[validate_unicode_slug
    ])
   
    def __str__(self):
        return self.nombre

class Estudiante_Gestion(models.Model):
 gestion=models.ForeignKey(Gestion,on_delete=models.CASCADE,related_name="Gestiones")
 estudiante=models.ForeignKey(Estudiante,on_delete=models.CASCADE,related_name="Estudiante")
 def __str__(self):
    return f"{self.gestion} - {self.estudiante}"

class Materia(models.Model):
   nombre=models.CharField(max_length=200)
   tipo=models.CharField(max_length=200)
   
   def __str__(self):
        return self.nombre

class Curso(models.Model):
   nombre=models.CharField(max_length=200)
   tipo=models.CharField(max_length=200)
   
   def __str__(self):
        return self.nombre
class Curso_Materia(models.Model):
   materia=models.ForeignKey(Materia,on_delete=models.CASCADE,related_name="materias")
   curso=models.ForeignKey(Curso,on_delete=models.CASCADE,related_name="cursos")
   def __str__(self):
    return f"{self.materia} - {self.curso}"
class notas(models.Model):
   valor=models.FloatField()
   tipo=models.CharField(max_length=50)
   est_gest=models.ForeignKey(Estudiante_Gestion,on_delete=models.CASCADE,related_name="gestionest")
   curs_mat=models.ForeignKey(Curso_Materia,on_delete=models.CASCADE,related_name="cursomateria")
   