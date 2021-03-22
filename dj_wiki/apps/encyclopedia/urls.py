from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki_entry, name="wiki_entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create_entry, name="create"),
    path("edit/<str:title>", views.edit_entry, name="edit"),
]
