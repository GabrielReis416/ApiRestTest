from django.db import models

class user(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=14)

    def __str__(self):
        return self.nome


'''
 id
 codigo do stream ( maximo 10 caracteres )
 descrição
 categoria ( Filmes, Series e Documentarios )
'''

class stream(models.Model):
    CATEGORIA = (
    ('F', 'Filme'),
    ('S', 'Serie'),
    ('D', 'Documentario'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=1, choices=CATEGORIA, blank=False, default='F')

    def __str__(self):
        return self.codigo
