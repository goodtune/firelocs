from django.urls import path

from firelocs.views import FireList, FireListJson, FireMap, drill_down_list

urlpatterns = [
    path("", FireList.as_view()),
    path("json/", FireListJson.as_view()),
    path("council/", drill_down_list),
    path("council/<council_area>/", drill_down_list, name="council"),
    path("map/", FireMap.as_view()),
]
