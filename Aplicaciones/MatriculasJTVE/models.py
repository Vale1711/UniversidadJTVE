from django.db import models

# Create your models here.
class carreraJTVE(models.Model):
    idCarreraJTVE=models.AutoField(primary_key=True)
    nombreCarreraJTVE=models.CharField(max_length=150)
    directorCarreraJTVE=models.CharField(max_length=150)
    logoCarreraJTVE=models.FileField(upload_to='carreraJTVE', null=True, blank=True)
    fechaFundacionCarreraJTVE = models.DateField()
    descripcionCarreraJTVE = models.TextField()


class cursoJTVE(models.Model):
    idCursoJTVE=models.AutoField(primary_key=True)
    nivelCursoJTVE=models.CharField(max_length=150)
    descripcionCursoJTVE=models.CharField(max_length=150)
    aulaCursoJTVE=models.CharField(max_length=150)
    pisoCursoJTVE = models.CharField(max_length=150)
    duracionCursoJTVE = models.CharField(max_length=150)
    carreraJTVE=models.ForeignKey(carreraJTVE,null=True,blank=True,on_delete=models.CASCADE)


class asignaturaJTVE(models.Model):
    idAsignaturaJTVE=models.AutoField(primary_key=True)
    nombreAsignaturaJTVE=models.CharField(max_length=150)
    creditosAsignaturaJTVE=models.CharField(max_length=150)
    fechaInicioAsignaturaJTVE=models.DateField()
    fechaFinalizacionAsignaturaJTVE=models.DateField()
    profesorAsignaturaJTVE=models.CharField(max_length=150)
    silaboAsignaturaJTVE=models.FileField(upload_to='pdfAsignaturaJTVE/')
    descripcionAsignaturaJTVE = models.TextField()
    tipoAsignaturaJTVE = models.CharField(max_length=150, null=True)
    cursoJTVE=models.ForeignKey(cursoJTVE,null=True,blank=True,on_delete=models.CASCADE)
