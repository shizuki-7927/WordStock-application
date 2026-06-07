from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Word


class WordListView(ListView):
    model = Word
    template_name = "words/word_list.html"
    context_object_name = "words"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(Q(word__icontains=query) | Q(meaning__icontains=query))
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
    fields = ["word", "meaning", "example"]


class WordUpdateView(UpdateView):
    model = Word
    template_name = "words/word_form.html"
    fields = ["word", "meaning", "example"]


class WordDeleteView(DeleteView):
    model = Word
    template_name = "words/word_confirm_delete.html"
    success_url = reverse_lazy("words:list")
