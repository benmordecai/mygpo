# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-24 02:07
from __future__ import unicode_literals

from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import migrations


def index_podcasts(apps, schema_editor):
    Podcast = apps.get_model("podcasts", "Podcast")
    Podcast.objects.update(search_vector=
        SearchVector('title', weight='A') +
        SearchVector('description', weight='B'),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0037_index_podcast_lastupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='search_vector',
            field=SearchVectorField(null=True),
        ),

		migrations.RunPython(index_podcasts),

        migrations.AlterField(
            model_name='podcast',
            name='search_vector',
            field=SearchVectorField(null=False),
        ),
    ]