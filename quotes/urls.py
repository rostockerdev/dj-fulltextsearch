from django.urls import path

from quotes.views.quote_list import QuoteList
from quotes.views.quote_search_multi_field import SearchQuoteMultiFieldList

app_name = "quotes"

urlpatterns = [
    path(
        "",
        QuoteList.as_view(),
        name="all_quotes",
    ),
    # from quotes.views.quote_search import SearchQuoteList
    # path("search", SearchQuoteList.as_view(), name="search_quote"),
    # Search single field
    # from quotes.views.quote_search_single_field import SearchQuoteSingleFieldList
    # path("search", SearchQuoteSingleFieldList.as_view(), name="search_quote"),
    path("search", SearchQuoteMultiFieldList.as_view(), name="search_quote"),
]
