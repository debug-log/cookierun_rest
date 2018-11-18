from django.db import models

class LogGame(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    cookie1st_id = models.IntegerField(default=-1)
    cookie2nd_id = models.IntegerField(default=-1)
    pet_id = models.IntegerField(default=-1)
    treasure1st_id = models.IntegerField(default=-1)
    treasure2nd_id = models.IntegerField(default=-1)
    treasure3rd_id = models.IntegerField(default=-1)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
