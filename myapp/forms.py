from django import forms

class VideoForm(forms.Form):
    message = forms.CharField(label="Текст для бегущей строки", max_length=50, required=True, initial='Hello World')
    width = forms.IntegerField(label="Ширина видео" ,min_value=100, required=True, initial=100)
    height = forms.IntegerField(label="Длина видео" ,min_value=100, required=True, initial=100)
    duration = forms.IntegerField(label="Длительность видео",min_value=1, required=True, initial=3)