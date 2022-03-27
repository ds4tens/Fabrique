from fabrique.settings import SENDER_URL, TOKEN
from fabrique.celery import app

from django.utils import timezone
from notifyer import models

import requests 
from requests import exceptions
from time import sleep
import json


@app.task
def filter_mailing(mailing_pk, flag = False):
    if flag:
        mailing = models.MailingModel.objects.get(pk=mailing_pk)
        op_code = mailing.op_code
        tag = mailing.tag 
        client_queryset = None

        if tag == '' and op_code == 0:
            client_queryset = models.Client.objects.all()
        elif tag == '':
            client_queryset = models.Client.objects.filter(operator_code=op_code )
        elif op_code == 0:
            client_queryset = models.Client.objects.filter(tag=tag)

        for client in client_queryset:
            sender.delay(client.id, mailing.id)

        if client_queryset is None:
            return 'filter_mailing каким-то чудом неверные данные в БД'
    return ('filter_mailing', True)

@app.task
def sender(client_id, mailing_id):
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        'Content-Type': 'application/json'
    }
    client = models.Client.objects.get(pk=client_id)
    mailing = models.MailingModel.objects.get(pk=mailing_id)
    message = models.Message(
        mailing_id=mailing,
        client_id=client,
        status = False
    )
    message.save()
    url = SENDER_URL+f'{message.id}'
    data = {
        'id': message.id,
        'phone': client.phone_number,
        'text': mailing.content
    }
    for _ in range(5):
        try:
            response = requests.post(
                url=url, headers=headers, 
                data=json.dumps(data) ,timeout=10
            )
        except exceptions.ConnectionError:
            sleep(15)
        except exceptions.TooManyRedirects:    
            sleep(300)
        except exceptions.Timeout:
            sleep(30)
        else:
            break

    if response.status_code == 200:
        message.status = True
        message.save()
        return ('sender', response.status_code)
    else:
        time = (mailing.finish_date - mailing.start_date)/4
        check_time.apply_async((mailing_id, True), eta=time)
    return ('sender', response.status_code)


@app.task
def check_time(mailing_id):
    mailing = models.MailingModel.objects.get(pk=mailing_id)
    if mailing.finish_date < timezone.now():
        filter_mailing.delay(filter_mailing, True)
    else:
        return (False, f'check_time {mailing_id} time has passed')