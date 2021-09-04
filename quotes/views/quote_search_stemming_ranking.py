from django.contrib.postgres import search
from django.views.generic import ListView

from quotes.models import Quote


class SearchResultsList(ListView):
    """Provide a list of quote with SearchVector and SearchRank search"""

    model = Quote
    context_object_name = "quotes"
    template_name = "quotes/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_vector = search.SearchVector("name", "quote")
        search_query = search.SearchQuery(query)
        return (
            Quote.objects.annotate(
                search=search_vector,
                rank=search.SearchRank(search_vector, search_query),
            )
            .filter(search=search_query)
            .order_by("-rank")
        )
