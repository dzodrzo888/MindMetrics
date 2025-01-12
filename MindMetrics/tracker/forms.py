from django import forms
from .models import MoodTracker

class MoodTrackerForm(forms.ModelForm):
    class Meta:
        model = MoodTracker
        fields = ['stress', 'anxiety', 'sleep', 'mood', 'physical', 'water', 'meal', 'nutrition']