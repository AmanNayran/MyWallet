from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    tipo_de_operacao_choices = [('C', 'Compra'), ('V', 'Venda')]
    tipo_de_operacao = forms.ChoiceField(choices=tipo_de_operacao_choices, label='Tipo de operação')

    class Meta:
        model = Transaction
        fields = ['data','stock', 'quantidade', 'preco_unitario', 'tipo_de_operacao', 'corretagem']

        Widgets = {
            'data': forms.DateInput(
                format=('%d/%m/%Y')
            )
        }
