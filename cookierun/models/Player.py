from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    lv = models.IntegerField(default=1, blank=True)
    exp = models.IntegerField(default=0, blank=True)
    crystal = models.IntegerField(default=0, blank=True)
    gold = models.IntegerField(default=0, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created_date',)
