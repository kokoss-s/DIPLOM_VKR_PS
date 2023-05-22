from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
#from django.db.models.signals import pre_save
#from django.dispatch import receiver


class Fire(models.Model):

    OBJECTS = {
        (1, 'Административное здание'),
        (2, 'Больница или школа'),
        (3, 'Библиотека или торговое предприятие'),
        (4, 'Склад льноволокна'),
        (5, 'Склад текстильных изделий'),
        (6, 'Склад резинотехнических изделий'),
        (7, 'Склад леса в штабелях'),
        (8, 'Склад пиломатериалов'),
        (9, 'Типография'),
        (10, 'Ремонтный зал ангара'),
    }

    name = models.CharField(
        verbose_name='Название пожара',
        max_length=50
    )
    time = models.IntegerField(
        verbose_name='Время с момента начала пожара',
        validators=[MinValueValidator(1), MaxValueValidator(60)],
        help_text='Введите время от 1 минуты до 60 минут',
    )
    corner = models.IntegerField(
        verbose_name='Угол распространения пожара',
        validators=[MinValueValidator(0), MaxValueValidator(180)],
        help_text='Введите значение от 0 градусов до 180 градусов',
    )
    object_type = models.PositiveSmallIntegerField(
        verbose_name='Объект пожара',
        choices=OBJECTS,
        blank=False,
        default=1
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        help_text='Необязательное поле'
    )

    class Meta:
        verbose_name = _("пожар")
        verbose_name_plural = _("пожары")

    def __str__(self):
        return self.name


class Calculate(models.Model):
    squere_first_ten = models.FloatField('Площадь пожара за первые 10 минут')
    squere = models.FloatField('Площадь пожара')
    perimeter = models.FloatField('Периметр пожара')
    front = models.FloatField('Фронт пожара')
    speed_of_squere = models.FloatField('Скорость роста площади пожара')
    line_speed = models.FloatField('Линейная скорость роста пожара')
    front_speed = models.FloatField('Скорость роста фронта пожара')
    object_type = models.CharField('Тип объекта', max_length=50)
    name = models.CharField('Название пожара', max_length=50)
    time = models.IntegerField('Время с момента начала пожара')
    corner = models.IntegerField('Угол распространения пожара')
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = _("Параметры пожара")
        verbose_name_plural = _("Параметры пожара")


#@receiver(pre_save, sender=Calculate)
#def update_fire_in_Calculate(sender, instance, **kwargs):
#    instance.fire = instance.Fire.id
