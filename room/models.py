from django.db import models

class Illuminance(models.Model):
    datetime = models.DateTimeField()
    status = models.FloatField()

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S') + ': ' + self.status

class Temperature(models.Model):
    datetime = models.DateTimeField()
    status = models.FloatField()

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S') + ': ' + self.status

class Pressure(models.Model):
    datetime = models.DateTimeField()
    status = models.FloatField()

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S') + ': ' + self.status