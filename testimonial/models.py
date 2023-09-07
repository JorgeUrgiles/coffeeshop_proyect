from django.db import models

# Create your models here.
class Testimonial(models.Model):
    name=models.CharField(max_length=100,verbose_name='Nombre')
    comment=models.TextField(verbose_name='comentario')
    image=models.ImageField(verbose_name="Foto de perfil",upload_to='testimonial')
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name="Testimonio"
        verbose_name_plural="Testimonios"
        ordering=["-created"]
    
    def __str__(self):
        return self.name
