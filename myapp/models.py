from django.db import models

# Create your models here.
class VideoRequest(models.Model):
    message = models.CharField(max_length=100, verbose_name='Текст сообщения')
    duration = models.IntegerField(verbose_name='Длительность видео в секундах')
    width = models.IntegerField(verbose_name='Ширина видео')
    height = models.IntegerField(verbose_name='Длина видео')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    file_name = models.CharField(max_length=100, verbose_name='Название файла видео')
    