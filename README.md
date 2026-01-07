# Hangman RPG

A simple Hangman web application with an RPG twist. This project is an improved version of the first project I created without help from tutorials.

<p align="center">
  <video 
    src="/assets/demo.mp4" 
    controls
    autoplay
    muted
    loop
    style="max-width: 100%;">
  </video>
</p>

### Tech Stack

- Framework: Django 6.0
- Frontend: Alpine.js, HTMX, Bootstrap, and NES.css
- Database: SQLite (Local/Dev)

The project includes a custom management command called `setup_words` to clear and seed the word and category database with the data provided. You may also add your own words and categories, provided that you follow the format.

### Key Features
- **A Retro RPG Twist**: replaces the traditional "gallows" with a dynamic 8-bit battle. Every correct guess leads to the enemy's defeat, while incorrect guesses will cause the enemy to damage the player, all styled within the NES.css CSS framework.
- **Seamless Asynchronous Gameplay**: Leverages HTMX to handle word guesses via AJAX, allowing the game to update the masked word's state and currently guessed letters without requiring a full page reload.
- **Reactive Frontend State**: uses Alpine JS to manage complex frontend triggers and events, such as enemy animations and sound effects.
- **Dynamic Word Management**: Includes a custom Django Management Command (`setup_words`) that clears and synchronizes the database with categorized word banks.

- **Themed Categories & Word Scaling**: Features multiple categories (e.g., Anime & Manga, Animals) with varying word lengths based on the chosen difficulty, pulling dynamically from a relational SQLite database.

### Installation & Setup

Follow these steps to get the game running locally.

1. **Clone the repository**

```
git clone https://github.com/LilliaBestGirl/hangman-game.git
cd hangman-game
```

2. **Set up the virtual environment**: Create and activate a Python virtual environment to keep the dependencies isolated from the global environment:

```
python -m venv .venv
source .venv/Scripts/activate # or .venv/Scripts/activate on Windows
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Environment Configuration**: The project requires a .env file to manage secrets.

- Copy the template: cp .env.example .env (or manually copy the contents).

- The default values in .env.example are pre-configured for local development, so no changes are strictly necessary to start.

5. **Initialize the database**: go to the main Django project folder and run the migrations and use the custom management command to seed the word bank.

```
cd hangman
python manage.py migrate
python manage.py setup_words
```

6. **Launch the Game**:

```
python manage.py runserver
```

### Future Improvements
- **User Authentication & Profiles**: Implementing a full account system to allow players to save their stats, track their win/loss ratios, and unlock retro-style achievements.

- **The "All-In" Guess Mechanic**: A high-risk, high-reward feature allowing players to attempt to solve the word in one go. A correct guess yields massive bonus points, but an incorrect guess results in an instant "Game Over."

- **Global Leaderboards**: A competitive scoring system using Django Aggregation to rank players globally based on points, categories cleared, and total victories.

- **Scoring System & Multipliers**: Introducing a point system that rewards speed, remaining health, and word difficulty, with "streak multipliers" for consecutive wins.

### Assets & Resources

- **Sprites & Animations**: [Skull Wolf Pixel Art](https://atari-boy.itch.io/skull-wolf-pixel-art) by **Atari Boy**.

- **Background Art**: [Forest/Mountain Landscape](https://opengameart.org/content/background-5) via OpenGameArt

- **Sound Design**:

  - Synthesized 8-bit effects created using [JSFXR](https://sfxr.me/)

  - Victory and defeat jingle, as well as incorrect buzz sound sourced from [Pixabay's 8-bit collection](https://atari-boy.itch.io/skull-wolf-pixel-art)

- **UI Framework**: [NES.css](https://nostalgic-css.github.io/NES.css/) for the authentic retro aesthetic.
