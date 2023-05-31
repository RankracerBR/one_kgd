from django.db import models

# Create your models here.

class Email(models.Model):
    nome = models.CharField(max_length = 100, default = 'Nome')
    email = models.EmailField(unique = True)
    congregacao = models.CharField(max_length = 100, default = "Congregacao" )

    def __str__(self):
        return self.nome
    
    def __str__(self):
        return self.congregacao
    
    def __str__(self):
        return self.email