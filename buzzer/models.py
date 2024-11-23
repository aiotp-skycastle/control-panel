from django.db import models

class Buzzer(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S')