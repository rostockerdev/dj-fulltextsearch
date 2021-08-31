from django.test import TestCase
from django.urls import reverse

from quotes.models import Quote


class QuoteModelTest(TestCase):
    def setUp(self) -> None:
        # Create two test quote
        self.quote1 = Quote.objects.create(
            name="Someone", quote="Someone once said something"
        )
        self.quote2 = Quote.objects.create(
            name="Sometwo", quote="Sometwo once said something"
        )

    def test_quote_model_name_field_correct(self):
        quote1 = Quote.objects.get(id=1)
        name_field_label = quote1._meta.get_field("name").verbose_name
        name_field_length = quote1._meta.get_field("name").max_length
        self.assertEqual(name_field_label, "Quotoer Name")
        self.assertEqual(name_field_length, 256)

    def test_quote_model_quote_field_correct(self):
        quote1 = Quote.objects.get(id=1)
        quote_field_label = quote1._meta.get_field("quote").verbose_name
        quote_field_length = quote1._meta.get_field("quote").max_length
        self.assertEqual(quote_field_label, "Quote Text")
        self.assertEqual(quote_field_length, 1024)

    def test_quote_object_correct(self):
        quote1 = Quote.objects.get(id=1)
        self.assertEqual(str(quote1), "Someone once said something")
