from django.urls import path

from quotes.views.quote_list import QuoteList
from quotes.views.quote_search import SearchQuoteList

app_name = "quotes"

urlpatterns = [
    path(
        "",
        QuoteList.as_view(),
        name="all_quotes",
    ),
    path("search", SearchQuoteList.as_view(), name="search_quote"),
]
