from django.db import models

# Create your models here.

class Promo(models.Model):
    nombre = models.CharField(max_length=200)
    celular = models.TextField(max_length=20)
    mail = models.TextField(max_length=100)
    mascota = models.TextField(max_length=50)
    comentario = models.CharField(max_length=200)
    
    class Meta:
        db_table = "promo_table"

    def __str__(self):
        return f"Nombre: {self.nombre}, Celular: {self.celular}, \
        Mail: {self.mail}, Mascota: {self.mascota}, Comentario: \
        {self.comentario}"

    
    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
        
