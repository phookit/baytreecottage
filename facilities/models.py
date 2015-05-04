from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class FacilitiesPage(Page, RichText):
    class Meta:
        verbose_name = _("Facilities page")
        verbose_name_plural = _("Facilities pages")


class Section(Orderable, RichText):
    facilitiespage = models.ForeignKey(FacilitiesPage, related_name="sections")
    title = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % self.title


class Image(Orderable):
    title = models.CharField(max_length=64)
    filename = models.FileField(upload_to='facilityimages')
    description = models.CharField(max_length=512, blank=True, null=True)
    section = models.ForeignKey(Section, related_name="images")

    def __str__(self):
        return "%s" % self.title
