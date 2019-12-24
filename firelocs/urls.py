from django.urls import path

from firelocs.views import FireList

urlpatterns = [
    path("", FireList.as_view()),
]
