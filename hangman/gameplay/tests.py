from django.test import TestCase
from django.urls import reverse
from .models import Word, Category, GameSession

# Create your tests here.

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

class CreateGameSessionTest(TestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(name='Animals')
        self.category_2 = Category.objects.create(name='Movies')

        self.word_1 = Word.objects.create(word='Shark', category=self.category_1, difficulty='EASY')
        self.word_2 = Word.objects.create(word='Elephant', category=self.category_1, difficulty='MEDIUM')
        self.word_3 = Word.objects.create(word='Lion', category=self.category_1, difficulty='EASY')

        self.word_4 = Word.objects.create(word='Toy Story', category=self.category_2, difficulty='EASY')
        self.word_5 = Word.objects.create(word="The Shawshank Redemption", category=self.category_2, difficulty='HARD')
        self.word_6 = Word.objects.create(word="The Spongebob Movie: Sponge Out of Water", category=self.category_2, difficulty='HARD')
        self.word_7 = Word.objects.create(word="The Lion King", category=self.category_2, difficulty='MEDIUM')

        self.url = reverse('create_game')

    def test_create_game_status_code(self):
        response = self.client.post(self.url, {'category': self.category_1.id, 'difficulty': 'EASY'})

        # Redirected
        self.assertEqual(response.status_code, 302)

        session = GameSession.objects.first()
        self.assertRedirects(response, reverse('game', kwargs={'pk': session.pk}))