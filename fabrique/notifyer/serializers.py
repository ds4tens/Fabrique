from rest_framework import serializers
from notifyer import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'phone_number', 'operator_code',
            'time_zone', 'tag',
        )
    # TODO сделать валидацию