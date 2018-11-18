from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cookierun.views import PlayerList, PlayerDetail
from cookierun.views import LogAccessList
from cookierun.views import LogGameList, LogBestScoreList
from cookierun.views import LogCookiePetTreasureList
from cookierun.views import LogCrystalGoldUsageList
from cookierun.views import LogDailyMissionList
from cookierun.views import LogCookiePetTreasureList
from cookierun.views import LogExperienceList

urlpatterns = [
    url(r'^player/$', PlayerList.as_view()),
    url(r'^player/(?P<pk>[a-z0-9]+)/$', PlayerDetail.as_view()),
    url(r'^logaccess/$', LogAccessList.as_view()),
    url(r'^loggame/$', LogGameList.as_view()),
    url(r'^logcookiepettreasure/$', LogCookiePetTreasureList.as_view()),
    url(r'^logcrystalgoldusage/$', LogCrystalGoldUsageList.as_view()),
    url(r'^logdailymission/$', LogDailyMissionList.as_view()),
    url(r'^logbestscore/$', LogBestScoreList().as_view()),
    url(r'^logexperience/$', LogExperienceList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
