from django.urls import path

from firelocs.views import FireList, FireListJson, drill_down_list

urlpatterns = [
    path("", FireList.as_view()),
    path("map/", FireList.as_view(template_name="firelocs/map_model.html")),
    path("json/", FireListJson.as_view()),
    path("council/", drill_down_list),
    path("council/<council_area>/", drill_down_list, name="council"),
]
