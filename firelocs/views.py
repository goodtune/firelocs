from django.http import JsonResponse
from django.views.generic.base import View
from django.views.generic.list import BaseListView, ListView

from firelocs.models import Incident


class FireList(ListView):
    model = Incident


class FireListJson(BaseListView, View):
    model = Incident

    def render_to_response(self, context, **response_kwargs):
        data = {each["id"]: each for each in self.get_queryset().values()}
        return JsonResponse(data)
