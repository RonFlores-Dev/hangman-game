from django import forms
from .models import GameSession

class GameSessionForm(forms.ModelForm):
    category = forms.CharField(max_length=50)
    difficulty = forms.CharField(max_length=10)

    class Meta:
        model = GameSession
        fields = ['category', 'difficulty']

class GuessForm(forms.ModelForm):
    last_guess = forms.CharField(max_length=1)

    class Meta:
        model = GameSession
        fields = ['last_guess']

    def clean_last_guess(self):
        letter = self.cleaned_data['last_guess'].upper()

        if not letter.isalpha():
            raise forms.ValidationError('Please enter a letter.')

        return letter