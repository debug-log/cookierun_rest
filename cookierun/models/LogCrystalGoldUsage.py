from django.db import models

class LogCrystalGoldUsage(models.Model):
    CRYSTAL_GOLD_TYPES = (
        ('crystal', 'crystal'),
        ('gold', 'gold'),
    )

    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    types = models.CharField(max_length=20, choices=CRYSTAL_GOLD_TYPES, default='gold')
    description = models.CharField(max_length=100)
    delta = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
