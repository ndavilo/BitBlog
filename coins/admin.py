from django.contrib import admin
from .models import Chart, Bitcoin, Binance, Tether, Ethereum

admin.site.register(Chart)
admin.site.register(Bitcoin)
admin.site.register(Binance)
admin.site.register(Tether)
admin.site.register(Ethereum)