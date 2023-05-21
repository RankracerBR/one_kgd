from django.db import models

# Create your models here.

class Email(models.Model):
    nome = models.CharField(max_length=100, default="Nome")
    sobrenome = models.CharField(max_length=100, default="Sobrenome")
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.sobrenome