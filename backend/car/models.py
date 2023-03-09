from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.conf import settings

User = get_user_model()


class Country(models.Model):
    """Страна производителя автомобиля"""
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    """Производитель автомобиля"""
    name = models.CharField(max_length=255, verbose_name='Имя', unique=True)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        verbose_name='Страна',
        related_name='brands',
        null=True
    )

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['name']

    def __str__(self):
        return self.name


class Car(models.Model):
    """Модель автомобиля"""
    name = models.CharField(max_length=255, verbose_name='Имя')
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Производитель',
        related_name='cars'
    )
    year_release = models.IntegerField(
        verbose_name='год начала выпуска',
        validators=[MaxValueValidator(timezone.now().year),
                    MinValueValidator(settings.MIN_YEAR_CAR)],
    )
    year_completion = models.IntegerField(
        verbose_name='Год окончания выпуска',
        validators=[MaxValueValidator(timezone.now().year),
                    MinValueValidator(settings.MIN_YEAR_CAR)],
        blank=True,
        null=True
    )
    base_price = models.IntegerField(
        verbose_name='Базовая цена',
        validators=[MinValueValidator(0, 'Цена не может быть меньше 0')],
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        if self.year_completion and self.year_release > self.year_completion:
            raise ValidationError(
                f'Год выпуска: {self.year_release} больше года завершения '
                f'выпуска: {self.year_completion}')
        return super().clean(*args, **kwargs)


class CarTTX(models.Model):
    """Технические характеристики автомобилей с двигателем внутреннего
    сгорания"""
    kpp_choices = (
        ('Ручная', 'Ручная'),
        ('Автоматическая', 'Автоматическая'),
        ('Робот', 'Робот')
    )
    car = models.OneToOneField(Car, on_delete=models.CASCADE,
                               verbose_name='Автомобиль',
                               related_name='carttx')
    door = models.IntegerField(
        verbose_name='Количество дверей',
        validators=[
            MinValueValidator(1, 'У автомобиля должна быть хотя бы 1 дверь'),
            MaxValueValidator(
                10, 'А вы видели автомобиль более чем 10 дверьми?')],
    )
    engine = models.IntegerField(
        verbose_name='Объем двигателя в куб. см',
        validators=[MinValueValidator(1, 'Ну хоть 1 кубик должен быть')]
    )
    cylinder = models.IntegerField(
        verbose_name='Количество цилиндров',
        validators=[MinValueValidator(1, 'Без поршней авто не поедет')],
    )
    kpp = models.CharField(choices=kpp_choices,
                           verbose_name='Тип коробки передач',
                           max_length=256, default=kpp_choices[0][1])

    class Meta:
        verbose_name = 'Технические характеристики'


class Comment(models.Model):
    """Комментарий к автомобилю"""
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        verbose_name='Автор',
        null=True,
        default=None
    )
    email = models.EmailField(max_length=254, verbose_name='Email',
                              default='anonymous')
    car = models.ForeignKey(
        Car,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Модель автомобиля'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    text = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:20]
