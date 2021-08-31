from django.test import TestCase
from django.urls import reverse

from quotes.models import Quote


class QuoteListViewTest(TestCase):
    def setUp(self) -> None:
        # Create two test quote
        self.quote1 = Quote.objects.create(
            name="Someone", quote="Someone once said something"
        )
        self.quote2 = Quote.objects.create(
            name="Sometwo", quote="Sometwo once said something"
        )

    def test_quote_list_url(self):
        response = self.client.get(reverse("quotes:all_quotes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quotes/quote.html")

    def test_quote_total(self):
        quote_total = Quote.objects.all().count()
        self.assertEqual(quote_total, 2)

    def test_quote_list_context(self):
        response = self.client.get(reverse("quotes:all_quotes"))
        self.assertTrue("quotes" in response.context)
        self.assertEqual(len(response.context["quotes"]), 2)
