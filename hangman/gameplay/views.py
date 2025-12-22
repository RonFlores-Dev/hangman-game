from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Word

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