from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Gestion,Estudiante,Estudiante_Gestion,Materia
from .serializer import GestionSerializer,EstudianteSerializer,Gest_EstudianteSerializer,MateriaSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
def index(request):
    return HttpResponse("hola mundo")

def Gestion1(request):
    post_sem=request.POST.get("sem")
    post_anio=request.POST.get("anio")
    
    if post_sem:
     if post_anio:
      gestion=Gestion(sem=post_sem,anio=post_anio)
      gestion.save()

    gest=Gestion.objects.all()
    return render(request,"Gestion.html",{
        "gestiones": gest
    })
# Create your views here.
class GestionViewset(viewsets.ModelViewSet):
   queryset=Gestion.objects.all()
   serializer_class=GestionSerializer

class EstudianteViewset(viewsets.ModelViewSet):
   queryset=Estudiante.objects.all()
   serializer_class=EstudianteSerializer

class EstudianteGestionViewset(viewsets.ModelViewSet):
   queryset=Estudiante_Gestion.objects.all()
   serializer_class=Gest_EstudianteSerializer

class MateriaCreateView(generics.CreateAPIView,generics.ListAPIView):
  queryset=Materia.objects.all()  
  serializer_class=MateriaSerializer   

#API CUSTOM
@api_view(['GET'])
def Estudiante_count(request):
   try:
      cantidad=Estudiante.objects.count()
      return JsonResponse({
         "cantidad":cantidad
      },
      safe=False,
      status=200
      )
   except Exception as e:
        return JsonResponse({"mensaje":str(e)},status=400)
