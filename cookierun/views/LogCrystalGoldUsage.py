from cookierun.models import *
from cookierun.serializers import *
from rest_framework import generics

class LogCrystalGoldUsageList(generics.ListCreateAPIView):
    queryset = LogCrystalGoldUsage.objects.all()
    serializer_class = LogCrystalGoldUsageSerializer

class LogCrystalGoldUsageDetail(generics.RetrieveDestroyAPIView):
    queryset = LogCrystalGoldUsage.objects.all()
    serializer_class = LogCrystalGoldUsageSerializer
