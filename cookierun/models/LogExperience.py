from django.db import models

class LogExperience(models.Model):
    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    lv = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
