from django.contrib import admin
from .models import Investor, Stock, Transaction

admin.site.register(Investor)
admin.site.register(Stock)
admin.site.register(Transaction)
