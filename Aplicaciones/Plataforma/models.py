from django.db import models

# Create your models here.
class Turno(models.Model):
    codigo=models.CharField(primary_key=True)
    dni=models.CharField()
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField()
    fecha=models.DateField()
    def __str__(self) -> str:
        return f"Turno: {self.codigo} {self.dni} {self.precio} {self.descripcion} {self.fecha}"

class Usuario(models.Model):
    dni=models.CharField(primary_key=True)
    contra=models.CharField(max_length=18)
    nombre=models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"Bienvenido: {self.dni} {self.contra}"

class Pofesional(models.Model):
    matricula=models.CharField(primary_key=True)
    especialidad=models.CharField()
    def __str__(self):
        return f"{self.matricula} {self.especialidad}"