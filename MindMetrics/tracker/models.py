from django.db import models
from django.contrib.auth.models import User

class MoodTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stress = models.IntegerField()
    anxiety = models.IntegerField()
    sleep = models.IntegerField()
    mood = models.IntegerField()
    physical = models.IntegerField()
    water = models.IntegerField()
    meal = models.CharField(max_length=255)
    nutrition = models.IntegerField()
    created_at = models.DateTimeField()
