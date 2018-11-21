from cookierun.models import LogOpenChest
from cookierun.serializers import LogOpenChestSerializer
from rest_framework import generics

class LogOpenChestList(generics.ListCreateAPIView):
    queryset = LogOpenChest.objects.all()
    serializer_class = LogOpenChestSerializer

class LogOpenChestDetail(generics.RetrieveDestroyAPIView):
    queryset = LogOpenChest.objects.all()
    serializer_class = LogOpenChestSerializer
