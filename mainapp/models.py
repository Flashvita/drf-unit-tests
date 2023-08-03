from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


TYPE_STATUS = (
    'new',
    'on moderation',
    'running',
    'stoped',
    'complete'
)
TYPE_STATUS_RUS = (
    'новая',
    'на модерации',
    'запущена',
    'остановлена',
    'завершена',
)
STATUS_CHOICES = list(zip(TYPE_STATUS, TYPE_STATUS_RUS))

class Company(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название компании'
    )
    phones = ArrayField(models.CharField(
        max_length=12,
        blank=True)
    ,size=10000)
    start_date = models.DateTimeField(verbose_name='Начало обзвона')
    end_date = models.DateTimeField(verbose_name='Окончание обзвона')
    status = models.CharField(
        default=TYPE_STATUS[0],
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name='Статус'
    )

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk':self.id})

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'





