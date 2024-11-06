from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Desk(models.Model):
    datetime = models.DateTimeField()

    def __str__(self):
        return self.datetime.strftime('%Y-%m-%d %H:%M:%S')

class Servo(models.Model):
    datetime = models.DateTimeField()
    angle = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(180)]
    )

    def __str__(self):
        return f"{self.angle} at {self.datetime}"