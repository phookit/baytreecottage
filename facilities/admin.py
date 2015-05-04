from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from .models import FacilitiesPage, Section, Image


class ImageInline(TabularDynamicInlineAdmin):
    model = Image


class SectionInline(TabularDynamicInlineAdmin):
    model = Section


class FacilitiesPageAdmin(PageAdmin):
    inlines = [
        SectionInline,
    ]

admin.site.register(FacilitiesPage, FacilitiesPageAdmin)
admin.site.register(Image)
