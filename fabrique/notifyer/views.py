from rest_framework import generics
from notifyer import serializers
from notifyer import models

# Create your views here.

class ClientApiView(generics.ListCreateAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
