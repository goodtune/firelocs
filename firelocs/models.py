from django.db import models


class Incident(models.Model):

    id = models.URLField(primary_key=True)
    published = models.DateTimeField()
    title = models.CharField(max_length=255)

    location = models.CharField(max_length=255)
    council_area = models.CharField(max_length=255)
    alert_level = models.CharField(max_length=255, null=True)

    latitude = models.DecimalField(max_digits=20, decimal_places=16)
    longitude = models.DecimalField(max_digits=20, decimal_places=16)

    fire_status = models.CharField(max_length=255, null=True)
    fire_type = models.CharField(max_length=255)
    fire_size = models.PositiveIntegerField()
    fire_agency = models.CharField(max_length=255)

    def __str__(self):
        return self.title
