from django.urls import path
from . import views
urlpatterns = [
    path('', views.generer_ics, name=""),
]
