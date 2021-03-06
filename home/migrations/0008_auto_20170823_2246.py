# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_generalsettings_site_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='featured_article',
            new_name='featured_recipe',
        ),
        migrations.AddField(
            model_name='homepage',
            name='num_recent_recipes',
            field=models.PositiveIntegerField(default=6),
        ),
    ]
