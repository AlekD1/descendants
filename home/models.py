from django.db import models


class Gallery(models.Model):
    title = models.CharField(
        verbose_name='Подпись',
        max_length=255,
    )

    image = models.ImageField(
        verbose_name='Изображение',
        max_length=255,
        upload_to="static/gallery"
    )


class Person(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )

    post = models.CharField(
        verbose_name='Должность',
        max_length=255,
    )

    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=255,
    )

    image = models.ImageField(
        verbose_name='Изображение',
        max_length=255,
        upload_to="static/person"
    )


class BoardOfTrustees(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )


class Feedback(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='Почта',
        max_length=255,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=50,
        null=True
    )
    message = models.TextField(
        verbose_name='Сообщение',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        blank=True
    )
    is_check = models.BooleanField(
        default=False,
        verbose_name = 'Просмотрено?'
    )

    class Meta:
        verbose_name = 'фидбэк'
        verbose_name_plural = 'Фидбэк'


class Contacts(models.Model):
    address = models.CharField(
        verbose_name='Адрес',
        max_length=255,
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
    )
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=255,
    )
