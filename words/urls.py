from django.urls import path

from .views import (
    GenreCreateView,
    GenreListView,
    GenreWordListView,
    WordCreateView,
    WordDeleteView,
    WordDetailView,
    WordListView,
    WordUpdateView,
)

app_name = "words"

urlpatterns = [
    path("", GenreListView.as_view(), name="genre_list"),
    path("genres/new/", GenreCreateView.as_view(), name="genre_create"),
    path("genres/<int:pk>/", GenreWordListView.as_view(), name="genre_words"),

    path("words/", WordListView.as_view(), name="list"),
    path("words/new/", WordCreateView.as_view(), name="create"),
    path("words/<int:pk>/", WordDetailView.as_view(), name="detail"),
    path("words/<int:pk>/edit/", WordUpdateView.as_view(), name="update"),
    path("words/<int:pk>/delete/", WordDeleteView.as_view(), name="delete"),
]