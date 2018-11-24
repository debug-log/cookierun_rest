from django.db import models

class Options(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
