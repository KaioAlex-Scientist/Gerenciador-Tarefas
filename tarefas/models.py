from django.db import models

class Tarefas(models.Model):

    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA", "Baixa"
        MEDIA = "MEDIA", "Media"
        Alta = "ALTA", "Alta"

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    concluida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    prioridade = models.CharField(max_length=10, choices=Prioridade.choices, default=Prioridade.BAIXA)

    def __str__(self):
        return  f"{self.titulo} - Prioridade {self.prioridade} "