# Generated by Django 3.2.10 on 2021-12-24 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Issue",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                (
                    "kind",
                    models.CharField(
                        blank=True,
                        choices=[("b", "Bug"), ("f", "Feature")],
                        default=None,
                        help_text="the kind of the issue",
                        max_length=1,
                        null=True,
                        verbose_name="kind",
                    ),
                ),
                ("priority", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Milestone",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("due_date", models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("due_date", models.DateField(blank=True, default=None, null=True)),
                (
                    "cost",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=None, max_digits=20, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MilestoneComment",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.CharField(max_length=255)),
                (
                    "milestone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tests.milestone"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="milestone",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="milestones",
                related_query_name="milestone",
                to="tests.project",
            ),
        ),
        migrations.CreateModel(
            name="IssueComment",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("comment", models.CharField(max_length=255)),
                (
                    "issue",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        related_query_name="comments",
                        to="tests.issue",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="issue",
            name="milestone",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="issues",
                related_query_name="issue",
                to="tests.milestone",
            ),
        ),
    ]