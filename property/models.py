from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    pure_phone = PhoneNumberField(
        "Нормализованный номер владельца",
        region="RU",
        blank=True,
        null=True,
    )
    new_building = models.CharField(
        "Новостройка",
        choices=[(None, "Неизвестно"), (True, "Новостройка"), (False, "Старое здание")],
        max_length=30,
        default=None,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        "Когда создано объявление",
        default=timezone.now,
        db_index=True,
    )

    description = models.TextField(
        "Текст объявления",
        blank=True,
    )
    price = models.IntegerField(
        "Цена квартиры",
        db_index=True,
    )

    town = models.CharField(
        "Город, где находится квартира", max_length=50, db_index=True
    )
    town_district = models.CharField(
        "Район города, где находится квартира",
        max_length=50,
        blank=True,
        help_text="Чертаново Южное",
    )
    address = models.TextField(
        "Адрес квартиры",
        help_text="ул. Подольских курсантов д.5 кв.4",
    )
    floor = models.CharField(
        "Этаж",
        max_length=3,
        help_text="Первый этаж, последний этаж, пятый этаж",
    )

    rooms_number = models.IntegerField(
        "Количество комнат в квартире",
        db_index=True,
    )
    living_area = models.IntegerField(
        "количество жилых кв.метров",
        null=True,
        blank=True,
        db_index=True,
    )

    has_balcony = models.BooleanField(
        "Наличие балкона",
        db_index=True,
        null=True,
        blank=True,
    )
    active = models.BooleanField(
        "Активно-ли объявление",
        db_index=True,
    )
    construction_year = models.IntegerField(
        "Год постройки здания",
        null=True,
        blank=True,
        db_index=True,
    )
    liked_by = models.ManyToManyField(
        User,
        verbose_name="Кто лайкнул",
        related_name="likes",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Complaint(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Кто жаловался",
        related_name="complaints",
        null=True,
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.SET_NULL,
        verbose_name="Квартира, на которую жаловались",
        related_name="complaints",
        null=True,
    )
    text = models.TextField(
        "Текст жалобы",
    )

    def __str__(self):
        return f"{self.author}, {self.flat}"


class Owner(models.Model):
    name = models.CharField(
        "ФИО владельца",
        max_length=200,
        db_index=True,
    )
    pure_phone = PhoneNumberField(
        "Нормализованный номер владельца",
        region="RU",
        blank=True,
        null=True,
        db_index=True,
    )
    flats = models.ManyToManyField(
        Flat,
        verbose_name="Квартиры в собственности",
        null=True,
        related_name="owners",
        db_index=True,
    )

    def __str__(self):
        return self.name
