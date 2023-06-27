from django.db import models
from django.contrib.auth.models import User
import re

class Investor(models.Model):
    PERFIL_DE_RISCO_CHOICES = (
        ('conservador', 'Conservador'),
        ('moderado', 'Moderado'),
        ('arrojado', 'Arrojado'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil_de_risco = models.CharField(max_length=20, choices=PERFIL_DE_RISCO_CHOICES)

def validate_cnpj(cnpj):
    # Remove caracteres que não são dígitos
    cnpj = re.sub(r'\D', '', cnpj)

    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        return False

    # Verifica se todos os dígitos são iguais
    if len(set(cnpj)) == 1:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(12):
        soma += int(cnpj[i]) * (5 - i % 6)
    resto = soma % 11
    if resto < 2:
        dv1 = 0
    else:
        dv1 = 11 - resto

    # Verifica o primeiro dígito verificador
    if int(cnpj[12]) != dv1:
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(13):
        soma += int(cnpj[i]) * (6 - i % 7)
    resto = soma % 11
    if resto < 2:
        dv2 = 0
    else:
        dv2 = 11 - resto

    # Verifica o segundo dígito verificador
    if int(cnpj[13]) != dv2:
        return False

    # CNPJ válido
    return True


class Stock(models.Model):
    codigo = models.CharField(max_length=6, unique=True, help_text='Código de 4 letras maiúsculas seguidas de 1 ou 2 números.')
    nome_empresa = models.CharField(max_length=100)
    cnpj_empresa = models.CharField(max_length=14, unique=True, help_text='Deve conter apenas números.')

    def clean(self):
        super().clean()

        # Valida o formato do código
        if not re.match(r'^[A-Z]{4}\d{1,2}$', self.codigo):
            raise ValidationError({'codigo': 'O código deve ter 4 letras maiúsculas seguidas de 1 ou 2 números.'})

        # # Valida o CNPJ
        # if not validate_cnpj(self.cnpj_empresa):
        #     raise ValidationError({'cnpj_empresa': 'O CNPJ é inválido.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.codigo

class Transaction(models.Model):
    OPERATION_CHOICES = [
        ('C', 'Compra'),
        ('V', 'Venda'),
    ]

    data = models.DateField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_operacao = models.CharField(max_length=1, choices=OPERATION_CHOICES)
    corretagem = models.DecimalField(max_digits=8, decimal_places=2)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data}\n{self.stock}\n{self.quantidade}\n{self.preco_unitario}\n{self.tipo_operacao}\n{self.corretagem}\n{self.investor}"



    