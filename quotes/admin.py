from django.contrib import admin

from quotes.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ["name", "quote"]


admin.site.register(Quote, QuoteAdmin)
