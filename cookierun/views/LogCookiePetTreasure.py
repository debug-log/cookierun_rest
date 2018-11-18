from cookierun.models import LogCookiePetTreasure
from cookierun.serializers import LogCookiePetTreasureSerializer
from rest_framework import generics

class LogCookiePetTreasureList(generics.ListCreateAPIView):
    queryset = LogCookiePetTreasure.objects.all()
    serializer_class = LogCookiePetTreasureSerializer

class LogCookiePetTreasureDetail(generics.RetrieveDestroyAPIView):
    queryset = LogCookiePetTreasure.objects.all()
    serializer_class = LogCookiePetTreasureSerializer
