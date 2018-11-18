from django.db import models

class LogDailyMission(models.Model):
    MISSION_REWARD_TYPES = (
        ('STEP_BY_STEP_REWARD', 'STEP_BY_STEP_REWARD'),
        ('ONLY_FINAL_REWARD', 'ONLY_FINAL_REWARD'),
    )

    MISSION_QUEST_TYPES = (
        ('OPTIONAL_QUEST', 'OPTIONAL_QUEST'),
        ('NOT_OPTIONAL_QUEST', 'NOT_OPTIONAL_QUEST'),
    )
    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    mission_reward_type = models.CharField(max_length=20, choices=MISSION_REWARD_TYPES, default='STEP_BY_STEP_REWARD')
    mission_quest_type = models.CharField(max_length=20, choices=MISSION_QUEST_TYPES, default='OPTIONAL_QUEST')
    mission_id = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
