from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Genre, Word


class GenreListView(ListView):
    model = Genre
    template_name = "words/genre_list.html"
    context_object_name = "genres"

    def get_queryset(self):
        return Genre.objects.annotate(word_count=Count("words")).order_by("name")


class GenreCreateView(CreateView):
    model = Genre
    template_name = "words/genre_form.html"
    fields = ["name"]
    success_url = reverse_lazy("words:genre_list")


class GenreWordListView(ListView):
    model = Word
    template_name = "words/genre_word_list.html"
    context_object_name = "words"
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        self.genre = get_object_or_404(Genre, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Word.objects.filter(genre=self.genre)
        query = self.request.GET.get("q", "").strip()

        if query:
            queryset = queryset.filter(
                Q(word__icontains=query) | Q(meaning__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genre"] = self.genre
        context["query"] = self.request.GET.get("q", "").strip()
        return context


class WordListView(ListView):
    model = Word
    template_name = "words/word_list.html"
    context_object_name = "words"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "").strip()

        if query:
            queryset = queryset.filter(
                Q(word__icontains=query) | Q(meaning__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        return context


class WordDetailView(DetailView):
    model = Word
    template_name = "words/word_detail.html"
    context_object_name = "word"


class WordCreateView(CreateView):
    model = Word
    template_name = "words/word_form.html"
    fields = ["genre", "word", "meaning", "example"]


class WordUpdateView(UpdateView):
    model = Word
    template_name = "words/word_form.html"
    fields = ["genre", "word", "meaning", "example"]


class WordDeleteView(DeleteView):
    model = Word
    template_name = "words/word_confirm_delete.html"
    success_url = reverse_lazy("words:genre_list")