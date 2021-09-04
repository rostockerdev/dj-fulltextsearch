from django.contrib.postgres import search
from django.contrib.postgres.search import SearchVector
from django.views.generic import ListView

from quotes.models import Quote


class SearchQuoteMultiFieldList(ListView):
    """Provide a list of quote with multi field search"""

    model = Quote
    context_object_name = "quotes"
    template_name = "quotes/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Quote.objects.annotate(search=SearchVector("name", "quote")).filter(
            search=query
        )
