from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contato'
        ordering = ['data_criacao']

    def __str__(self):
        return f'{self.nome} - {self.email}'