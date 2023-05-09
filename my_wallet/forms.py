from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    tipo_de_operacao_choices = [('C', 'Compra'), ('V', 'Venda')]
    tipo_de_operacao = forms.ChoiceField(choices=tipo_de_operacao_choices, label='Tipo de operação')
    quantidade_de_acoes = forms.IntegerField(min_value=1, label='Quantidade de ações')

    class Meta:
        model = Transaction
        fields = ['stock', 'quantidade_de_acoes', 'preco_unitario', 'tipo_de_operacao', 'corretagem']
