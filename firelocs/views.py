from django.views.generic.list import ListView

from firelocs.models import Incident


class FireList(ListView):
    model = Incident
