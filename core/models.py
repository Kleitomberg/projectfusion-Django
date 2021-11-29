from django.db import models

import uuid
# Create your models here.

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField("Data de modificação", auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self) :
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) :
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name = 'Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField("Imagem", upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Funcionalidade(Base):

    ICONE_CHOICE = (
        ('lni-rocket','Foguete'),
        ('lni-laptop-phone','Computador'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf','Folha'),
        ('lni-layers','Camadas'),        
    )

    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', max_length=100)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = 'Funcionalidade'
        verbose_name_plural = 'Funcionalidades'

    def __str__(self):
        return self.nome