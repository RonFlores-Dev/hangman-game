from django.test import TestCase
from django.urls import reverse
from .models import Word, Category

# Create your tests here.

class GameViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Animals')
        self.test_word = Word.objects.create(word='Shark', category=self.category, difficulty='EASY')
        self.url = reverse('index')

    def test_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_word_is_masked(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['masked_word'], '_____')

    def test_masked_word_is_in_view(self):
        response = self.client.get(self.url)
        self.assertContains(response, '_____')