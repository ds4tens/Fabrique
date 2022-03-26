from rest_framework import serializers
from django.forms import ValidationError
from django.utils import timezone
import pytz
from notifyer import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'phone_number', 'operator_code',
            'time_zone', 'tag',
        )
    
    def validate(self, attrs):
        phone = str(attrs['phone_number'])
        if phone[0] != '7':
            raise ValidationError(f'{phone} номер не начинается с 7')

        if len(phone) != 11:
            raise ValidationError(f'{phone} номер должен составлять 11 символов')
        
        if attrs['time_zone'] not in pytz.common_timezones_set:
            raise ValidationError('{} not in {}'.format(attrs['time_zone'], pytz.common_timezones_set))

        return super().validate(attrs)

class MailingSerialaizer(serializers.ModelSerializer):
    op_code = serializers.IntegerField(default=0)
    tag = serializers.CharField(allow_blank=True)
    class Meta:
        model = models.MailingModel
        fields = (
            'content',
            'start_date', 'finish_date',
            'tag', 'op_code',
        )
    
    def validate(self, attrs):
        """Проверка корректности времени начала и конца"""
        if attrs["start_date"] >= attrs["finish_date"]:
            raise ValidationError("Дата начала превышает дату окончания")
        
        if attrs["finish_date"] <= timezone.now():
                raise ValidationError(
                    "Дата окончания рассылки уже пройдена"
                    "мы записываем бесполезные данные"
                )
        if attrs['op_code'] != 0:
            if len(str(attrs['op_code'])) != 3:
                raise ValidationError('Код оператора должен быть 3 символа')

        return super().validate(attrs)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"