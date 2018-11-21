from django.db import models

class LogOpenChest(models.Model):
    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    types = models.CharField(max_length=20, default='gold_chest')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
