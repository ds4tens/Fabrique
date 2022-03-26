from rest_framework import generics, mixins, viewsets
from notifyer import serializers
from notifyer import models

# Create your views here.

class ClientApiView(generics.ListCreateAPIView):
    # TODO переделать под сет
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

class MailingViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = models.MailingModel.objects.all()
    serializer_class = serializers.MailingSerialaizer
