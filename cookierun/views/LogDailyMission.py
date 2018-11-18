from cookierun.models import LogDailyMission
from cookierun.serializers import LogDailyMissionSerializer
from rest_framework import generics

class LogDailyMissionList(generics.ListCreateAPIView):
    queryset = LogDailyMission.objects.all()
    serializer_class = LogDailyMissionSerializer

class LogDailyMissionDetail(generics.RetrieveDestroyAPIView):
    queryset = LogDailyMission.objects.all()
    serializer_class = LogDailyMissionSerializer
