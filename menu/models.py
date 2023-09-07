from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=50, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=["name"]

    def __str__(self):
        return self.name


class Menu(models.Model):
    TYPE_FOOD=[
      ('food', 'Food'),     # El primer valor ('foos') es el valor almacenado en la base de datos, 
        ('drinks', 'Drinks'),]
    
    price=models.CharField(max_length=6,verbose_name="Precio")
    name=models.CharField(max_length=50, verbose_name="Nombre")
    description=models.CharField(max_length=200,verbose_name="Descripcion")
    image=models.ImageField(verbose_name="Image",upload_to="menu")
    type=models.CharField(max_length=6,choices=TYPE_FOOD,default='food')
    categories=models.ManyToManyField(Category, verbose_name=("Categorias"))
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificacion")

    
    
    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering=["created"]
        
    
    def __str__(self):
        return self.name




