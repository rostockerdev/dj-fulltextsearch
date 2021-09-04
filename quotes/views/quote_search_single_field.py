from django.views.generic import ListView

from quotes.models import Quote


class SearchQuoteSingleFieldList(ListView):
    """Provide a list of quote with single field search"""

    model = Quote
    context_object_name = "quotes"
    template_name = "quotes/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Quote.objects.filter(quote__search=query)
