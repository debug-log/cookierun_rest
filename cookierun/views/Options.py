from cookierun.models import *
from cookierun.serializers import *
from rest_framework import generics

class OptionsList(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
