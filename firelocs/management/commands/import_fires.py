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
        "alert_level": data["ALERT LEVEL"].strip(),
        "fire_status": data["STATUS"].strip(),
        "fire_type": data["TYPE"].strip(),
        "fire_size": HA_RE.search(data["SIZE"]).groups()[0],
        "fire_agency": data["RESPONSIBLE AGENCY"].strip(),
    }


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
                **summary_to_kwargs(entry.summary)
            )
            for entry in feed.entries
        ]
        Incident.objects.all().delete()
        Incident.objects.bulk_create(objs)
