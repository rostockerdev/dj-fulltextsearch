from django.urls import path

from quotes.views import QuoteList

app_name = "quotes"

urlpatterns = [
    path(
        "",
        QuoteList.as_view(),
        name="all_quotes",
    )
]
