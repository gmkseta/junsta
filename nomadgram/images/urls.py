from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("feed/", view=views.Feed.as_view(), name="feeds"),
]