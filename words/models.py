from django.db import models
from django.urls import reverse


class Word(models.Model):
    word = models.CharField("単語・言葉", max_length=100)
    meaning = models.TextField("意味・定義")
    example = models.TextField("具体例・例文", blank=True)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "単語"
        verbose_name_plural = "単語"

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        return reverse("words:detail", kwargs={"pk": self.pk})
