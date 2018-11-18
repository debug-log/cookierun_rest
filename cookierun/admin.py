from django.contrib import admin
from cookierun.models import *

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'lv', 'exp', 'crystal', 'gold', 'created_date')

class LogAccessAdmin(admin.ModelAdmin):
    list_display = ('pname', 'types', 'date')

class LogGameAdmin(admin.ModelAdmin):
    list_display = ('pname', 'score', 'cookie1st_id', 'cookie2nd_id', 'pet_id', 'treasure1st_id', 'treasure2nd_id', 'treasure3rd_id', 'date',)

class LogCookiePetTreasureAdmin(admin.ModelAdmin):
    list_display = ('pname', 'equip_id', 'lv', 'amount', 'date')

class LogCrystalGoldUsageAdmin(admin.ModelAdmin):
    list_display = ('pname', 'types', 'description', 'delta', 'result', 'date')

class LogDailyMissionAdmin(admin.ModelAdmin):
    list_display = ('pname', 'mission_reward_type', 'mission_quest_type', 'mission_id', 'date',)

class LogExperienceAdmin(admin.ModelAdmin):
    list_display = ('pname', 'lv', 'exp', 'date')

admin.site.register(Player, PlayerAdmin)
admin.site.register(LogAccess, LogAccessAdmin)
admin.site.register(LogGame, LogGameAdmin)
admin.site.register(LogCookiePetTreasure, LogCookiePetTreasureAdmin)
admin.site.register(LogCrystalGoldUsage, LogCrystalGoldUsageAdmin)
admin.site.register(LogDailyMission, LogDailyMissionAdmin)
admin.site.register(LogExperience, LogExperienceAdmin)
