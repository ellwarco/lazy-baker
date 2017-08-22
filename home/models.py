from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

from recipes.models import RecipePage, CaptionedImageBlock


class HomePage(Page):
    parent_page_types = ['wagtailcore.Page']

    body = RichTextField(blank=True)
    featured_article = models.ForeignKey(
        RecipePage,
        null=True, blank=True,
        on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        PageChooserPanel('featured_article'),
    ]

    class Meta:
        verbose_name = "Homepage"

    def latest_articles(self):
        articles = RecipePage.objects.live()
        articles = articles.order_by('-date')
        return articles[0:5]


@register_setting
class GeneralSettings(BaseSetting):
    site_name = models.CharField(
        max_length=127,
        help_text='Website name')
    '''favicon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Icon for site in browsers (Must be .ico file to work)',
    )'''
    site_tagline = models.CharField(
        max_length=255,
        blank=True,
        help_text='Tagline to show after the site title'
    )
    site_description = models.TextField(
        blank=True,
        help_text='Description of website (to appear on searches)',
    )
    pagination_count = models.PositiveIntegerField(
        default=10,
        help_text="Number of posts to display per page on index pages")
    disqus = models.CharField(
        max_length=127,
        null=True, blank=True,
        help_text="Site name on Disqus. Comments will only appear if this is provided.")
    google_analytics_id = models.CharField(
        max_length=127,
        blank=True, null=True,
        help_text='Google Analytics Tracking ID')
    google_custom_search_key = models.CharField(
        max_length=127,
        blank=True, null=True,
        help_text='Unique ID for Google Custom Search')

    panels = [
        FieldPanel('site_name'),
        #ImageChooserPanel('favicon'),
        FieldPanel('site_tagline'),
        FieldPanel('site_description'),
        FieldPanel('pagination_count'),
        FieldPanel('disqus'),
        FieldPanel('google_analytics_id'),
        FieldPanel('google_custom_search_key'),
    ]