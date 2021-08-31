from django.shortcuts import render
from django.views.generic import ListView

from quotes.models import Quote


class QuoteList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "quotes/quote.html"
