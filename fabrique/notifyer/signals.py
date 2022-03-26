from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from notifyer import models
from notifyer.cetasks import filter_mailing

@receiver(post_save, sender=models.MailingModel)
def notify(sender, instance, created, **kwargs):

    current_time = timezone.now()

    if created:
        start = instance.start_date
        finish = instance.finish_date

        if start <= current_time and finish > current_time:
            filter_mailing.delay(instance.id, True)
        else:
            filter_mailing.apply_async((instance.id, True), eta=start)

    else:
        # TODO Продумать как обновлять очередь если были изменения в БД
        pass