from ...models import Word, Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the database with words per categories'

    def handle(self, *args, **options):
        data = {
            'Animals': [
                ('Shark', 'EASY'),
                ('Elephant', 'EASY'),
                ('Lion', 'EASY'),
                ('Tiger', 'EASY'),
                ('Python', 'EASY'),

                ('Cassowary', 'MEDIUM'),
                ('Axolotl', 'MEDIUM'),
                ('King Cobra', 'MEDIUM'),
                ('Polar Bear', 'MEDIUM'),
                ('Orangutan', 'MEDIUM'),

                ('Great White Shark', 'HARD'),
                ('Philippine Eagle', 'HARD'),
                ('Huntsman Spider', 'HARD'),
                ('Silverback Gorilla', 'HARD'),
                ('Tarantula Hawk Wasp', 'HARD')
            ],
            'Anime & Manga': [
                ('Naruto', 'EASY'),
                ('Bleach', 'EASY'),
                ('Inuyasha', 'EASY'),
                ('Fairy Tail', 'EASY'),
                ('One Piece', 'EASY'),

                ('Chainsaw Man', 'EASY'),
                ('Death Note', 'MEDIUM'),
                ('Jujutsu Kaisen', 'MEDIUM'),
                ('Boruto: Two Blue Vortex', 'MEDIUM'),
                ('Attack on Titan', 'MEDIUM'),

                ('JoJo\'s Bizzare Adventure', 'HARD'),
                ('I Want to End This Love Game', 'HARD'),
                ('The Angel Next Door Spoils Me Rotten', 'HARD'),
                ('Frieren: Beyond Journey\'s End', 'HARD'),
                ('Kaguya-sama: Love is War', 'HARD'),
            ],
            'Video Games': [
                ('Minecraft', 'EASY'),
                ('Overwatch', 'EASY'),
                ('Fortnite', 'EASY'),
                ('Terraria', 'EASY'),
                ('Spore', 'EASY'),

                ('Super Mario Bros.', 'MEDIUM'),
                ('Poppy Playtime', 'MEDIUM'),
                ('League of Legends', 'MEDIUM'),
                ('Stardew Valley', 'MEDIUM'),
                ('Grand Theft Auto V', 'MEDIUM'),

                ('Five Nights at Freddy\'s: Secret of the Mimic', 'HARD'),
                ('The Legend of Zelda: Breath of the Wild', 'HARD'),
                ('Counter-Strike: Global Offensive', 'HARD'),
                ('Star Wars: The Force Unleashed', 'HARD'),
                ('Clair Obscur: Expedition 33', 'HARD'),
            ],
            "Movies": [
                ('The Avengers', 'EASY'),
                ('The Matrix', 'EASY'),
                ('Interstellar', 'EASY'),
                ('Toy Story', 'EASY'),
                ('Shrek', 'EASY'),

                ('Jurassic Park', 'MEDIUM'),
                ('The Dark Knight', 'MEDIUM'),
                ('Flushed Away', 'MEDIUM'),
                ('The Incredibles', 'MEDIUM'),
                ('A Bug\'s Life', 'MEDIUM'),

                ('A Nightmare on Elm Street', 'HARD'),
                ('Puss in Boots: The Last Wish', 'HARD'),
                ('How to Train Your Dragon', 'HARD'),
                ('The Shawshank Redemption', 'HARD'),
                ('The SpongeBob Movie: Sponge Out of Water', 'HARD'),
            ]
        }

        for category, words in data.items():
            category, _ = Category.objects.get_or_create(name=category)
            for word, difficulty in words:
                Word.objects.get_or_create(
                    category=category,
                    word=word,
                    difficulty=difficulty)
            
        self.stdout.write(self.style.SUCCESS('Words populated successfully!'))