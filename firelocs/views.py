from django.http import JsonResponse
from django.template.response import TemplateResponse
from django.views.generic.base import TemplateView, View
from django.views.generic.list import BaseListView, ListView

from firelocs.models import Incident


class FireList(ListView):
    model = Incident


class FireListJson(BaseListView, View):
    model = Incident

    def render_to_response(self, context, **response_kwargs):
        data = {each["id"]: each for each in self.get_queryset().values()}
        return JsonResponse(data)


def drill_down_list(request, council_area=None):
    object_list = Incident.objects.all()
    context = {
        "object_list": object_list,
        "council_area": council_area,
    }
    return TemplateResponse(request, "firelocs/incident_drill.html", context)
