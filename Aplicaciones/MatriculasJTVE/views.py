from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def carrera(request):
    carreras=carreraJTVE.objects.all()
    return render(request,'carrera.html',{'carreras':carreras, 'navbar': 'carrera'})

def guardarCarrera(request):
    nombreCarreraJTVE=request.POST["nombreCarreraJTVE"]
    directorCarreraJTVE=request.POST["directorCarreraJTVE"]
    logoCarreraJTVE=request.FILES.get("logoCarreraJTVE")
    fechaFundacionCarreraJTVE=request.POST["fechaFundacionCarreraJTVE"]
    descripcionCarreraJTVE=request.POST["descripcionCarreraJTVE"]


    nuevoCarrera=carreraJTVE.objects.create(nombreCarreraJTVE=nombreCarreraJTVE, directorCarreraJTVE=directorCarreraJTVE, logoCarreraJTVE=logoCarreraJTVE,
                                          fechaFundacionCarreraJTVE=fechaFundacionCarreraJTVE, descripcionCarreraJTVE=descripcionCarreraJTVE)


    return redirect('/carrera')

def eliminarCarrera(request,idCarreraJTVE):
    carreraEliminar=carreraJTVE.objects.get(idCarreraJTVE=idCarreraJTVE)
    carreraEliminar.delete()
    messages.success(request, 'Carrera eliminado exitosamente')
    return redirect('/carrera')

def editarCarrera(request, idCarreraJTVE):
    carreraEditar=carreraJTVE.objects.get(idCarreraJTVE=idCarreraJTVE)
    return render(request, 'editarCarrera.html', {'carrera': carreraEditar})

def procesarinformacionCarrera(request):
    idCarreraJTVE=request.POST["idCarreraJTVE"]
    nombreCarreraJTVE=request.POST["nombreCarreraJTVE"]
    directorCarreraJTVE=request.POST["directorCarreraJTVE"]
    logoCarreraJTVE=request.FILES.get("logoCarreraJTVE")
    fechaFundacionCarreraJTVE=request.POST["fechaFundacionCarreraJTVE"]
    descripcionCarreraJTVE=request.POST["descripcionCarreraJTVE"]
    #Insertando datos mediante el ORM de DJANGO
    carreraEditar=carreraJTVE.objects.get(idCarreraJTVE=idCarreraJTVE)
    carreraEditar.nombreCarreraJTVE=nombreCarreraJTVE
    carreraEditar.directorCarreraJTVE=directorCarreraJTVE
    if 'logoCarreraJTVE' in request.FILES:
            logoCarreraJTVE = request.FILES.get("logoCarreraJTVE")
    else:
            # Si no se proporciona una nueva imagen, conserva la existente
            in_existente = carreraJTVE.objects.get(idCarreraJTVE=idCarreraJTVE)
            logoCarreraJTVE = in_existente.logoCarreraJTVE
    carreraEditar.fechaFundacionCarreraJTVE=fechaFundacionCarreraJTVE
    carreraEditar.descripcionCarreraJTVE=descripcionCarreraJTVE
    carreraEditar.save()
    messages.success(request,
      'Carrera ACTUALIZADO Exitosamente')
    return redirect('/carrera')

def curso(request):
    cursos=cursoJTVE.objects.all()
    carreras=carreraJTVE.objects.all()
    return render(request,'curso.html',{'cursos':cursos, 'carreras': carreras,'navbar': 'curso'})

def guardarCurso(request):
    id_carrera=request.POST["id_carrera"]
    cursoSeleccionado=carreraJTVE.objects.get(idCarreraJTVE=id_carrera)
    nivelCursoJTVE=request.POST["nivelCursoJTVE"]
    descripcionCursoJTVE=request.POST["descripcionCursoJTVE"]
    aulaCursoJTVE=request.POST["aulaCursoJTVE"]
    pisoCursoJTVE=request.POST["pisoCursoJTVE"]
    duracionCursoJTVE=request.POST["duracionCursoJTVE"]


    nuevoCurso=cursoJTVE.objects.create(nivelCursoJTVE=nivelCursoJTVE, descripcionCursoJTVE=descripcionCursoJTVE, aulaCursoJTVE=aulaCursoJTVE,
                                          pisoCursoJTVE=pisoCursoJTVE, duracionCursoJTVE=duracionCursoJTVE, carreraJTVE=cursoSeleccionado)
    return redirect('/curso')

def eliminarCurso(request,idCursoJTVE):
    cursoEliminar=cursoJTVE.objects.get(idCursoJTVE=idCursoJTVE)
    cursoEliminar.delete()
    messages.success(request, 'Curso eliminado exitosamente')
    return redirect('/curso')

def editarCurso(request, idCursoJTVE):
    cursoEditar=cursoJTVE.objects.get(idCursoJTVE=idCursoJTVE)
    carreras=carreraJTVE.objects.all()
    return render(request, 'editarCurso.html', {'curso': cursoEditar, 'carreras': carreras})

def procesarinformacionCurso(request):
    idCursoJTVE=request.POST["idCursoJTVE"]
    id_carrera=request.POST["id_carrera"]
    cursoSeleccionado=carreraJTVE.objects.get(idCarreraJTVE=id_carrera)
    nivelCursoJTVE=request.POST["nivelCursoJTVE"]
    descripcionCursoJTVE=request.POST["descripcionCursoJTVE"]
    aulaCursoJTVE=request.POST["aulaCursoJTVE"]
    pisoCursoJTVE=request.POST["pisoCursoJTVE"]
    duracionCursoJTVE=request.POST["duracionCursoJTVE"]
    #Insertando datos mediante el ORM de DJANGO
    cursoEditar=cursoJTVE.objects.get(idCursoJTVE=idCursoJTVE)
    cursoEditar.carreraJTVE=cursoSeleccionado
    cursoEditar.nivelCursoJTVE=nivelCursoJTVE
    cursoEditar.descripcionCursoJTVE=descripcionCursoJTVE
    cursoEditar.aulaCursoJTVE=aulaCursoJTVE
    cursoEditar.pisoCursoJTVE=pisoCursoJTVE
    cursoEditar.duracionCursoJTVE=duracionCursoJTVE
    cursoEditar.save()
    messages.success(request,
      'Curso ACTUALIZADO Exitosamente')
    return redirect('/curso')

def asignatura(request):
    asignaturas=asignaturaJTVE.objects.all()
    cursos=cursoJTVE.objects.all()
    return render(request,'asignatura.html',{'asignaturas':asignaturas, 'cursos': cursos,'navbar': 'asignatura'})

def guardarAsignatura(request):
    id_curso=request.POST["id_curso"]
    curSeleccionado=cursoJTVE.objects.get(idCursoJTVE=id_curso)
    nombreAsignaturaJTVE=request.POST["nombreAsignaturaJTVE"]
    creditosAsignaturaJTVE=request.POST["creditosAsignaturaJTVE"]
    fechaInicioAsignaturaJTVE=request.POST["fechaInicioAsignaturaJTVE"]
    fechaFinalizacionAsignaturaJTVE=request.POST["fechaFinalizacionAsignaturaJTVE"]
    profesorAsignaturaJTVE=request.POST["profesorAsignaturaJTVE"]
    silaboAsignaturaJTVE=request.FILES.get("silaboAsignaturaJTVE")
    descripcionAsignaturaJTVE=request.POST["descripcionAsignaturaJTVE"]
    tipoAsignaturaJTVE=request.POST["tipoAsignaturaJTVE"]


    nuevoAsignatura=asignaturaJTVE.objects.create(nombreAsignaturaJTVE=nombreAsignaturaJTVE, creditosAsignaturaJTVE=creditosAsignaturaJTVE, fechaInicioAsignaturaJTVE=fechaInicioAsignaturaJTVE,
                                          fechaFinalizacionAsignaturaJTVE=fechaFinalizacionAsignaturaJTVE, profesorAsignaturaJTVE=profesorAsignaturaJTVE, silaboAsignaturaJTVE=silaboAsignaturaJTVE,
                                          descripcionAsignaturaJTVE=descripcionAsignaturaJTVE, tipoAsignaturaJTVE=tipoAsignaturaJTVE, cursoJTVE=curSeleccionado)
    return redirect('/asignatura')

def eliminarAsignatura(request,idAsignaturaJTVE):
    asignaturaEliminar=asignaturaJTVE.objects.get(idAsignaturaJTVE=idAsignaturaJTVE)
    asignaturaEliminar.delete()
    messages.success(request, 'Curso eliminado exitosamente')
    return redirect('/asignatura')

def editarAsignatura(request, idAsignaturaJTVE):
    asignaturaEditar=asignaturaJTVE.objects.get(idAsignaturaJTVE=idAsignaturaJTVE)
    cursos=cursoJTVE.objects.all()
    return render(request, 'editarAsignatura.html', {'asignatura': asignaturaEditar, 'cursos': cursos})

def procesarinformacionAsignatura(request):
    idAsignaturaJTVE=request.POST["idAsignaturaJTVE"]
    id_curso=request.POST["id_curso"]
    curSeleccionado=cursoJTVE.objects.get(idCursoJTVE=id_curso)
    nombreAsignaturaJTVE=request.POST["nombreAsignaturaJTVE"]
    creditosAsignaturaJTVE=request.POST["creditosAsignaturaJTVE"]
    fechaInicioAsignaturaJTVE=request.POST["fechaInicioAsignaturaJTVE"]
    fechaFinalizacionAsignaturaJTVE=request.POST["fechaFinalizacionAsignaturaJTVE"]
    profesorAsignaturaJTVE=request.POST["profesorAsignaturaJTVE"]
    silaboAsignaturaJTVE=request.FILES.get("silaboAsignaturaJTVE")
    descripcionAsignaturaJTVE=request.POST["descripcionAsignaturaJTVE"]
    tipoAsignaturaJTVE=request.POST["tipoAsignaturaJTVE"]
    #Insertando datos mediante el ORM de DJANGO
    asignaturaEditar=asignaturaJTVE.objects.get(idAsignaturaJTVE=idAsignaturaJTVE)
    asignaturaEditar.cursoJTVE=curSeleccionado
    asignaturaEditar.nombreAsignaturaJTVE=nombreAsignaturaJTVE
    asignaturaEditar.creditosAsignaturaJTVE=creditosAsignaturaJTVE
    asignaturaEditar.fechaInicioAsignaturaJTVE=fechaInicioAsignaturaJTVE
    asignaturaEditar.fechaFinalizacionAsignaturaJTVE=fechaFinalizacionAsignaturaJTVE
    asignaturaEditar.profesorAsignaturaJTVE=profesorAsignaturaJTVE
    if silaboAsignaturaJTVE:
        asignaturaEditar.silaboAsignaturaJTVE = silaboAsignaturaJTVE
    asignaturaEditar.descripcionAsignaturaJTVE=descripcionAsignaturaJTVE
    asignaturaEditar.tipoAsignaturaJTVE=tipoAsignaturaJTVE
    asignaturaEditar.save()
    messages.success(request,
      'Asignatura ACTUALIZADO Exitosamente')
    return redirect('/asignatura')
