from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from .models import Car,CarInventory
from django.db import models
from django.db.models import Sum

def car_inventory_update():
    car_count = Car.objects.count()
    car_value = Car.objects.aggregate(total_value=Sum('price'))['total_value'] or 0.00

    CarInventory.objects.create(cars_count=car_count, cars_value=car_value)
    print(f'Inventário atualizado: {car_count} carros, valor total R${car_value:.2f}')


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
    
@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Sem descrição disponível."


