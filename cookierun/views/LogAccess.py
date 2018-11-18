from cookierun.models import LogAccess
from cookierun.serializers import LogAccessSerializer
from rest_framework import generics

class LogAccessList(generics.ListCreateAPIView):
    queryset = LogAccess.objects.all()
    serializer_class = LogAccessSerializer

class LogAccessDetail(generics.RetrieveDestroyAPIView):
    queryset = LogAccess.objects.all()
    serializer_class = LogAccessSerializer
