from django.urls import path
from .views import GameView, GameSessionDetailView, UpdateGameSessionView

urlpatterns = [
    path('', GameView.as_view(), name='index'),
    path('game/<int:pk>', GameSessionDetailView.as_view(), name='game'),
    path('guess/<int:pk>/', UpdateGameSessionView.as_view(), name='guess_letter'),
]