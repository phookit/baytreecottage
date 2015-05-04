from django.contrib import admin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import HomePage, Slide, Statement


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class StatementInline(TabularDynamicInlineAdmin):
    model = Statement


class HomePageAdmin(PageAdmin):
    inlines = (StatementInline, SlideInline)

admin.site.register(HomePage, HomePageAdmin)

