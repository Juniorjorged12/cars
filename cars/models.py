from django.db import models

# Create your models here.
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, related_name='car_brand')
    year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    plate = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class CarInventory(models.Model):
    cars_count = models.IntegerField(default=0)
    cars_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Inventario em {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}: {self.cars_count} carros, valor total R${self.cars_value}"