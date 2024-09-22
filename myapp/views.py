from django.shortcuts import render
import cv2
import numpy as np
import os
from django.conf import settings

from django.http import FileResponse,HttpResponse, Http404, HttpResponseBadRequest
from .forms import VideoForm

def create_video(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VideoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            message = form.cleaned_data['message']
            width = form.cleaned_data['width']
            height = form.cleaned_data['height']
            duration = form.cleaned_data['duration']

            video_path = create_text_video_opencv(message,width,height,duration)
            
            if os.path.exists(video_path):
                return FileResponse(open(video_path, 'rb'), as_attachment=True, filename=f"{message}.mp4")
                # with open(video_path, 'rb') as fh:
                #     # response = HttpResponse(fh.read(), content_type="application/force-download")
                #     # response['Content-Disposition'] = f'attachment; filename=' + os.path.basename(file_path)
                #     response = HttpResponse(fh.read(), content_type='video/mp4')
                #     response['Content-Disposition'] = f'attachment; filename={text}.mp4'
                #     return response
            raise Http404

    # if a GET (or any other method) we'll create a blank form
    else:
        form = VideoForm()

    return render(request, 'index.html', {'form': form})
    
    
    
    
    
    

def create_text_video_opencv(message, width, height, video_length):
    # Текст для вывода
    # message = request.GET.get('text')
    # Параметры видео
    # width, height = 100, 100  # Разрешение видео
    fps = 24  # Кадров в секунду
    # video_length = 3  # Длительность видео в секундах

    # Рассчитаем общее количество кадров
    total_frames = video_length * fps
    output_path = os.path.join(settings.MEDIA_ROOT, f"{message}.mp4")
    # Настройка видеопотока
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    
    
    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Настройки шрифта
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  # Белый цвет текста

    # Получаем размер текста
    (text_width, text_height), _ = cv2.getTextSize(message, font, font_scale, font_thickness)

    # Рассчитываем начальную позицию и скорость текста
    x_start = width  # Начинаем с правого края экрана
    x_end = -text_width  # Заканчиваем, когда текст полностью выйдет за левый край

    # Рассчитываем общее расстояние, которое должен пройти текст, и скорость за кадр
    total_distance = x_start - x_end
    speed_per_frame = total_distance / total_frames

    # Вертикальная позиция для текста (по центру вертикали)
    y = height // 2 + text_height // 2

    # Проходим по каждому кадру
    for t in range(total_frames):
        # Очищаем кадр (черный фон)
        frame.fill(0)

        # Рассчитываем новую координату x для текста
        x = int(x_start - t * speed_per_frame)

        # Отображаем текст на кадре
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        # Записываем кадр в видео
        out.write(frame)

    # Освобождаем видеопоток
    out.release()
    
    return output_path
