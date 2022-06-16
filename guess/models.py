from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_color(value):
    if value.capitalize() != 'Красный' and value.capitalize() != 'Синий' \
        and value.capitalize() != 'Зеленый':
        raise ValidationError(
            _("Цвет должен быть 'Красный','Синий' или 'Зеленый' "))
        
def validate_number(value):
    if value < 1 or value > 100:
        raise ValidationError(
            _('Значение должно быть в диапазоне от 1 до 100'))

class Item(models.Model):
    number = models.IntegerField(unique=True,
                                 validators=[validate_number])
    color = models.CharField(max_length=7,
                             validators=[validate_color])
    


