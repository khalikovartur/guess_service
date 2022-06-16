from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Item


def validate_number(value):
    if value < 1 or value > 100:
        raise ValidationError(
            _('Значение должно быть в диапазоне от 1 до 100'))
        

class NumberPostForm(forms.Form):
   num_item = forms.IntegerField(label='Номер предмета',
                            validators=[validate_number])
   
   
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('number', 'color')
                           
    