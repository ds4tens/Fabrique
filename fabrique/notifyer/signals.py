from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from notifyer import models

@receiver(post_save, sender=models.MailingModel)
def notify(sender, instance, created, **kwargs):

    current_time = timezone.now()

    if created:
        start = instance.start_date
        finish = instance.finish_date

        if start <= current_time and finish > current_time:
            ...
        else:
            ...
    else:
        # TODO разобраться как удалять или обновлять очередь
        pass