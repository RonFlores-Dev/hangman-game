from django.test import TestCase
from django.urls import reverse
from .models import Word, Category, GameSession

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

class UpdateGameSessionTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Animals')
        self.test_word = Word.objects.create(word='Shark', category=self.category, difficulty='EASY')
        self.test_session = GameSession.objects.create(word=self.test_word, masked_word='_____', guessed_letters='', lives=5, result='START')
        self.url = reverse('guess_letter', args=[self.test_session.id])

    def test_masked_word_status(self):
        response = self.client.post(self.url, {'last_guess': 'a'}, HTTP_HX_REQUEST='true')

        self.assertEqual(response.status_code, 200)

    def test_masked_word_is_updated(self):
        response = self.client.post(self.url, {'last_guess': 'a'}, HTTP_HX_REQUEST='true')
        self.test_session.refresh_from_db()

        self.assertEqual(self.test_session.masked_word, '__A__')

    def test_masked_word_is_updated_twice(self):
        response = self.client.post(self.url, {'last_guess': 'a'}, HTTP_HX_REQUEST='true')
        self.test_session.refresh_from_db()
        self.assertEqual(self.test_session.masked_word, '__A__')

        response = self.client.post(self.url, {'last_guess': 'k'}, HTTP_HX_REQUEST='true')
        self.test_session.refresh_from_db()
        self.assertEqual(self.test_session.masked_word, '__A_K')