from cookierun.models import LogGame
from cookierun.serializers import LogGameSerializer
from rest_framework import generics
from django.db.models.aggregates import Max

class LogGameList(generics.ListCreateAPIView):
    queryset = LogGame.objects.all()
    serializer_class = LogGameSerializer

class LogBestScoreList(generics.ListAPIView):
    serializer_class = LogGameSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = LogGame.objects.all().values('pname').annotate(score=Max('score')).order_by('-score')
        pnames = [item['pname'] for item in queryset]
        scores = [item['score'] for item in queryset]
        return LogGame.objects.filter(pname__in = pnames, score__in = scores).order_by('-score')