# Generated manually for the initial Word model.

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Word",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("word", models.CharField(max_length=100, verbose_name="単語・言葉")),
                ("meaning", models.TextField(verbose_name="意味・定義")),
                ("example", models.TextField(blank=True, verbose_name="具体例・例文")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="登録日時")),
            ],
            options={
                "verbose_name": "単語",
                "verbose_name_plural": "単語",
                "ordering": ["-created_at"],
            },
        ),
    ]
