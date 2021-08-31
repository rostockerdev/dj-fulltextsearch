from django.core.management.base import BaseCommand
from faker import Faker

from quotes.models import Quote


class Command(BaseCommand):
    help = "Add quotes in Database"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(100):
            Quote.objects.create(name=fake.name(), quote=fake.text())

        print("Insertion Completed ...")
