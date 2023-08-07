from django.shortcuts import render, redirect
from random import randint
from .models import LabeledSentence

def get_unlabeled_sentence():
    # 라벨링되지 않은 문장 중에서 랜덤하게 하나를 선택하여 반환합니다.
    total_sentences = LabeledSentence.objects.count()
    while True:
        random_index = randint(0, total_sentences - 1)
        random_sentence = LabeledSentence.objects.all()[random_index]
        if not random_sentence.emotion:
            return random_sentence.sentence

def label_sentence(request):
    if request.method == 'POST':
        sentence = request.POST['sentence']
        emotion = request.POST['emotion']
        LabeledSentence.objects.create(sentence=sentence, emotion=emotion)
        return redirect('label_sentence')


    unlabeled_sentence = get_unlabeled_sentence()
    return render(request, 'labeling/label_sentence.html', {'sentence': unlabeled_sentence})
