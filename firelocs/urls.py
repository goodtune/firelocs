from django.urls import path

from firelocs.views import FireList, FireListJson

urlpatterns = [
    path("", FireList.as_view()),
    path("json/", FireListJson.as_view()),
]
