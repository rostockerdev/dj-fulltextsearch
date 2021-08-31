from django.db import models


class Quote(models.Model):
    """Model representing a single quote"""

    name = models.CharField("Quotoer Name", max_length=256)
    quote = models.CharField("Quote Text", max_length=1024)

    def __str__(self) -> str:
        return self.quote
