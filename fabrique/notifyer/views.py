from rest_framework import generics, mixins, viewsets
from django.db.models import Count
from notifyer import models
from notifyer import serializers

# Create your views here.

class ClientViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin,
                    mixins.ListModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class MailingViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = models.MailingModel.objects.all()
    serializer_class = serializers.MailingSerialaizer

class MessageToMailingStatView(generics.ListAPIView):
    """Информация об отправленных сообщениях опредленной рассылки"""
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        mailing_id = self.request.data['mailing_id']
        return models.Message.objects.filter(mailing_id=mailing_id)

class MessageStatView(generics.ListAPIView):
    """Статистика по рассылке и статусу"""
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        queryset = models.Message.objects.values('mailing_id', 'status').annotate(count=Count('id'))
        return queryset

class MessageAllView(generics.ListAPIView):
    serializer_class = serializers.MessageSerializer
    queryset = models.Message.objects.all()