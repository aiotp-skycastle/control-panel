from django.db import models

class Chair(models.Model):
    datetime = models.DateTimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S') + ': ' + self.status