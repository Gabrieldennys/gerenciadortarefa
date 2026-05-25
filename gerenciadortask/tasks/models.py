from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(max_length=200)

    descricao = models.TextField()

    prazo = models.IntegerField()

    concluida = models.BooleanField(default=False)

    criada_em = models.DateTimeField(auto_now_add=True)

    concluida_em = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo

