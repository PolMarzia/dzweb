from django.forms import ModelForm
from mainsite.models import *

class skazka_form(ModelForm):
    class Meta:
        model = skazka_dar
        fields = ['name', 'author', 'image', 'text']
        labels = {
            'name' : 'Название',
            'author' : 'Автор',
            'image' : 'Картинка',
            'text' : 'Текст'
        }