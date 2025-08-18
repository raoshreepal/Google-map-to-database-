from django.db import models
from .scraper import scrape_google_maps

class Business(models.Model):
    maps_url = models.URLField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.name:  # scrape only if empty
            data = scrape_google_maps(self.maps_url)
            self.name = data.get("name")
            self.address = data.get("address")
            self.contact = data.get("contact")
            self.website = data.get("website")
            self.email = data.get("email")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else self.maps_url
