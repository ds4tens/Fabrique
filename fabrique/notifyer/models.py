from django.db import models

# Create your models here.


class Client(models.Model):
    """ Моделька получателя 'клиент' """
    phone_number = models.IntegerField()
    operator_code = models.SmallIntegerField()
    # FIXME нужно будет придумать вариант реализации через выборку
    time_zone = models.SmallIntegerField() # часовой пояс будет вычисляться вычетанием по модулю
    tag = models.CharField(max_length=32, default='')

class MailingModel(models.Model):
    """ Моделька рассылки """
    content = models.TextField('Текст сообщения') 
    start_date = models.DateTimeField('Время начала')
    finish_date = models.DateTimeField('Время конца')

    """ Для тэга и операторского кода возможен выбор пустого поля """
    tag = models.CharField('Тэг', max_length=32) # предполагаю текстовая метка
    op_code = models.IntegerField(blank=True, null=True) 

class Message(models.Model):
    """ 
    Модель сообщений
    При удалении клиента или рассылки данные не будут удален из статистики
    """
    mailing_id = models.ForeignKey(MailingModel, verbose_name='id рассылки', on_delete=models.DO_NOTHING)
    client_id = models.ForeignKey(Client, verbose_name='id клиента', on_delete=models.DO_NOTHING)
    date_creation = models.DateTimeField(auto_now=True)
    status = models.BooleanField('Статус')
    