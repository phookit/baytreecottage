from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.models import RichText
from mezzanine.pages.models import Page

class MapLocal(Page, RichText):
    class Meta:
        verbose_name = _("Map And Local")
        verbose_name_plural = _("Map and locals")
