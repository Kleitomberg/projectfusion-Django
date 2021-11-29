# Generated by Django 3.2.9 on 2021-11-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-rocket', ''), ('lni-laptop-phone', ''), ('lni-cog', ''), ('lni-leaf', ''), ('lni-layers', '')], max_length=20, verbose_name='Icone')),
            ],
            options={
                'verbose_name': 'Funcionalidade',
                'verbose_name_plural': 'Funcionalidades',
            },
        ),
    ]
