from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre de la marca")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    class Meta:
            verbose_name = 'Marca'
            verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre del departamento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre del producto")
    brand = models.ForeignKey(Brand, verbose_name=("Marca"),default=1,on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name=("Departamento"),default=1,on_delete=models.CASCADE)
    visible = models.BooleanField(verbose_name="Visible")
    amount = models.DecimalField(max_digits=5, decimal_places=2,verbose_name="Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.name
        
