from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # question에 연결된 답변이기 때문에 foreignKey로 설정.
    # "on_delete=models.CASCADE"를 추가하면 answer와 연결된 question이 삭제될 경우 answer도 함께 삭제 됨
    content = models.TextField()
    create_date = models.DateTimeField()