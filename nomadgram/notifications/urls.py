from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", view=views.Notifications.as_view(), name="notifications"),

]

