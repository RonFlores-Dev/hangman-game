from django.urls import path
from .views import (GameView, GameSessionDetailView, CreateGameSessionView,
                    UpdateGameSessionView)

urlpatterns = [
    path('', CreateGameSessionView.as_view(), name='create_game'),
    path('game/<int:pk>', GameSessionDetailView.as_view(), name='game'),
    path('guess/<int:pk>/', UpdateGameSessionView.as_view(), name='guess_letter'),
]