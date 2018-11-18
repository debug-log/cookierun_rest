from django.db import models

class LogAccess(models.Model):
    LOG_TYPES = (
        ('login', 'login'),
        ('logout', 'logout'),
    )

    pname = models.ForeignKey('Player', on_delete=models.CASCADE)
    types = models.CharField(max_length=20, choices=LOG_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)
