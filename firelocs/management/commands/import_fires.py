import re
from datetime import datetime
from time import mktime

import feedparser
from django.core.management.base import BaseCommand, CommandError
from html2text import html2text

from firelocs.models import Incident

HA_RE = re.compile(r"(\d+) ha")
KV_RE = re.compile(r"(.+?): (.+)")


def summary_to_kwargs(summary):
    """
    Extract key-value pairs from the description field (which is HTML)
    """
    data = dict(
        [
            match.groups()
            for match in [
                KV_RE.search(line) for line in html2text(summary).splitlines()
            ]
            if match
        ]
    )
    return {
        "location": data["LOCATION"].strip(),
        "council_area": data["COUNCIL AREA"].strip(),
        "fire_type": data["TYPE"].strip(),
        "fire_size": HA_RE.search(data["SIZE"]).groups()[0],
        "fire_agency": data["RESPONSIBLE AGENCY"].strip(),
    }

def extract_latitude(entry):
    return lat_lon_from_entry(entry)[1]

def extract_longitude(entry):
    return lat_lon_from_entry(entry)[0]

def lat_lon_from_entry(entry):
    """
    Provide a lat lon regardless of the georss type presented by feedparser

    Feedparser only populates the "where" field with the last georss element
    rather than passing on each different element type. This means that the
    coordinates attribute may be a single-element tuple containing a list of
    tuples (lon, lat) if the last element is a polygon, or a tuple (lon, lat)
    if the last element is a point. Even thought it's not perfect, we will
    pass through the first tuple of the polygon if we have a polygon and the
    point if it's a point. Yuk.
    """
    if entry.where["type"] == "Point":
        return entry.where["coordinates"]

    # Assume it's a polygon
    return entry.where["coordinates"][0][0]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("source")

    def handle(self, source, *args, **options):
        feed = feedparser.parse(source)
        objs = [
            Incident(
                id=entry.id,
                published=datetime.fromtimestamp(mktime(entry.published_parsed)),
                title=entry.title,
                longitude=extract_longitude(entry),
                latitude=extract_latitude(entry),
                **summary_to_kwargs(entry.summary)
            )
            for entry in feed.entries
        ]
        Incident.objects.all().delete()
        Incident.objects.bulk_create(objs)
