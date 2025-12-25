from json import dumps
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView
from .models import Word, GameSession
from .forms import GuessForm, GameSessionForm

# Create your views here.

class GameView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word_obj = Word.objects.order_by('?').first()

        if word_obj:
            word_text = word_obj.word.upper()
            context['category'] = word_obj.category.name
            context['word'] = word_text
            context['masked_word'] = "".join([' ' if c == ' ' or not c.isalpha() else '_' for c in word_text])
            context['word_id'] = word_obj.id
        
        return context
    
class GameSessionDetailView(DetailView):
    model = GameSession
    context_object_name = 'game_session'
    template_name = 'game.html'
    
class CreateGameSessionView(CreateView):
    model = GameSession
    form_class = GameSessionForm

    def form_valid(self, form):
        return super().form_valid(form)
    
class UpdateGameSessionView(UpdateView):
    model = GameSession
    form_class = GuessForm
    template_name = 'index.html'

    def form_valid(self, form):
        session = self.get_object()

        letter = form.cleaned_data['last_guess'].upper()
        target_word = session.word.word.upper()
        current_mask = session.masked_word

        is_correct = letter in target_word
        result = ''

        if letter.isalpha() and letter not in session.guessed_letters:
            session.guessed_letters += letter
            
            if letter in target_word:
                new_mask = ""
                for target_char, mask_char in zip(target_word, current_mask):
                    if target_char == letter:
                        new_mask += letter
                    else:
                        new_mask += mask_char
                
                session.masked_word = new_mask
                is_correct = True
                result = 'CORRECT'
            else:
                session.lives -= 1
                is_correct = False
                result = 'INCORRECT'

            # Win/Loss Check
            if session.lives <= 0:
                result = 'DEFEAT'
            elif session.masked_word == target_word:
                result = 'VICTORY'

            session.result = result
        
        session.save()

        if self.request.headers.get('HX-Request'):
            context = self.get_context_data(
                object=session,
                guessed_letter=letter,
                status='is-success' if is_correct else 'is-error'
            )
            
            self.template_name = 'partials/masked-word.html'

            response = self.render_to_response(context)
            trigger_data = { 
                "game-state-changed": {
                    "action": result
                }
            }

            response['HX-Trigger'] = dumps(trigger_data)

            return response
        
        # return super().form_valid(form)
        
    def form_invalid(self, form):
        if self.request.headers.get('HX-Request'):
            return self.render_to_response(
                self.get_context_data(form=form),
                status=422
            )

        return super().form_invalid(form)    