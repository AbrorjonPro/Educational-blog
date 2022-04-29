from django.db.models.signals import pre_delete, post_delete
from .models import (
    Articles,
    Books,
    Presentations,
    Projects,
    Videos,
)                                                   # signal sender

from django.dispatch import receiver

@receiver(pre_delete, sender=Articles)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()
    if instance.file_uz:
        instance.file_uz.delete()
    if instance.file_ru:
        instance.file_ru.delete()
    if instance.file_en:
        instance.file_en.delete()

@receiver(pre_delete, sender=Books)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()
    if instance.file_uz:
        instance.file_uz.delete()
    if instance.file_ru:
        instance.file_ru.delete()
    if instance.file_en:
        instance.file_en.delete()

@receiver(pre_delete, sender=Presentations)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()
    if instance.file_uz:
        instance.file_uz.delete()
    if instance.file_ru:
        instance.file_ru.delete()
    if instance.file_en:
        instance.file_en.delete()
        
@receiver(pre_delete, sender=Projects)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()
    if instance.file_uz:
        instance.file_uz.delete()
    if instance.file_ru:
        instance.file_ru.delete()
    if instance.file_en:
        instance.file_en.delete()

# @receiver(pre_delete, sender=Events)
# def delete_file(sender, instance, **kwargs):
#     if instance.file:
#         instance.file.delete()
#     if instance.file_uz:
#         instance.file_uz.delete()
#     if instance.file_ru:
#         instance.file_ru.delete()
#     if instance.file_en:
#         instance.file_en.delete()

@receiver(pre_delete, sender=Videos)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete()
    if instance.file_uz:
        instance.file_uz.delete()
    if instance.file_ru:
        instance.file_ru.delete()
    if instance.file_en:
        instance.file_en.delete()