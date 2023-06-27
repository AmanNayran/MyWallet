from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('transactions/;', views.transactions, name='transactions'),
    path('transacao/<int:transacao_id>/', views.transaction_detail, name='transaction_detail'),
    path('transacao/<int:transacao_id>/editar', views.transaction_edit, name='transaction_edit'),
    path('transacao/<int:transacao_id>/remover/', views.transaction_remove, name='transaction_remove'),
]
