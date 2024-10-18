from django.urls import path
from .views import hello_word  # Certifique-se de que o caminho para a view está correto

app_name = 'rest_api'

urlpatterns = [
    path('hello/', hello_word, name='hello_word'),
]