from django.db import models

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page


class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    nicknames = blocks.ListBlock(blocks.CharBlock())


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock()),
        ('person', PersonBlock()),
        ('shopping_list', blocks.ListBlock(blocks.CharBlock())),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
