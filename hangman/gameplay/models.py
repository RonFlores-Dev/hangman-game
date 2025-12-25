from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Word(models.Model):
    choices = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=choices)

    def __str__(self):
        return self.word
    
class GameSession(models.Model):
    choices = [
        ('START', 'Start'),
        ('VICTORY', 'Victory'),
        ('DEFEAT', 'Defeat'),
        ('CORRECT', 'Correct'),
        ('INCORRECT', 'Incorrect'),
    ]

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    masked_word = models.CharField(max_length=100)
    guessed_letters = models.CharField(max_length=26, default='', blank=True)
    lives = models.IntegerField()
    result = models.CharField(max_length=10, choices=choices, default='START')

    def __str__(self):
        return f"Game Session for {self.word}"