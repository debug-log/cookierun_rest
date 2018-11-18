from cookierun.models import *
from cookierun.serializers import *
from rest_framework import generics

class LogExperienceList(generics.ListCreateAPIView):
    queryset = LogExperience.objects.all()
    serializer_class = LogExperienceSerializer

class LogExperienceDetail(generics.RetrieveDestroyAPIView):
    queryset = LogExperience.objects.all()
    serializer_class = LogExperienceSerializer
