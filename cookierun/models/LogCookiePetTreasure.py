from django.db import models

class LogCookiePetTreasure(models.Model):
    
    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    equip_id = models.CharField(max_length=20, default="cookie0001")
    lv = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
