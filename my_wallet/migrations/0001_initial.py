# Generated by Django 4.2.1 on 2023-05-09 01:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text='Código de 4 letras maiúsculas seguidas de 1 ou 2 números.', max_length=6, unique=True)),
                ('nome_empresa', models.CharField(max_length=100)),
                ('cnpj_empresa', models.CharField(help_text='Deve conter apenas números.', max_length=14, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil_de_risco', models.CharField(choices=[('conservador', 'Conservador'), ('moderado', 'Moderado'), ('arrojado', 'Arrojado')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
