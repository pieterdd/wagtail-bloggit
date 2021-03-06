# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 10:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0012_copy_image_permissions_to_collections'),
        ('wagtailcore', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('post_date', models.DateTimeField()),
                ('post_body', wagtail.wagtailcore.fields.StreamField([('text_blob', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock())])),
                ('primary_visual', models.ForeignKey(blank=True, help_text='Can be shown on overview pages or in feeds.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
