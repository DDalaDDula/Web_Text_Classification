from django.urls import path
from ..labeling import views

urlpatterns = [
    path('label_sentence/', views.label_sentence, name='label_sentence'),
]
