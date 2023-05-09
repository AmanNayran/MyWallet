from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    stocks = Stock.objects.all()
    context = {
        'user': user,
        'stocks': stocks,
    }
    return render(request, 'dashboard.html', context)


from .models import Transaction
from .forms import TransactionForm

@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'add_transaction.html', {'form': form})



@login_required
def transactions(request):
    transactions = Transaction.objects.filter(investor=request.user.investor)
    return render(request, 'transactions.html', {'transactions': transactions})

@login_required
def transaction_detail(request, transacao_id):
    transaction = get_object_or_404(Transaction, id=transacao_id, investor=request.user.investor)
    return render(request, 'transaction_detail.html', {'transaction': transaction})

@login_required
def transaction_edit(request, transacao_id):
    transacao = get_object_or_404(Transaction, id=transacao_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transacao)
        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form = TransactionForm(instance=transacao)
    return render(request, 'transaction_edit.html', {'form': form})

@login_required
def transaction_remove(request, transacao_id):
    transacao = get_object_or_404(Transaction, id=transacao_id)
    transacao.delete()
    return redirect('transactions')