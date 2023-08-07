from django.db import models

class LabeledSentence(models.Model):
    sentence = models.TextField()
    emotion = models.CharField(max_length=20)  # 예: 'Happy', 'Sad', 'Neutral'

    def __str__(self):
        return self.sentence