from rest_framework import serializers
from notifyer import models
from django.forms import ValidationError

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'phone_number', 'operator_code',
            'time_zone', 'tag',
        )
    
    # TODO если поле timezone будет реализовано через словарь, то нужно сделат еще проверку
    def validate(self, attrs):
        phone = str(attrs['phone_number'])
        if phone[0] != '7':
            raise ValidationError(f'{phone} номер не начинается с 7')

        if len(phone) != 11:
            raise ValidationError(f'{phone} номер должен составлять 11 символов')
        
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
    
    # TODO validate

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"