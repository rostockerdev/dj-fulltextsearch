from django.db.models import Q
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView

from quotes.models import Quote


class SearchQuoteList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "quotes/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Quote.objects.filter(
            Q(name__icontains=query) | Q(quote__icontains=query)
        )
