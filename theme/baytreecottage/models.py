from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
    change_over_day = models.CharField(max_length=32)

    class Meta:
        verbose_name = _("Home Page")
        verbose_name_plural = _("Home Pages")

        
class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    caption = models.CharField(max_length=64, null=True, blank=True)
    text_colour = models.CharField(max_length=15, default='#ffffff', null=True, blank=True, verbose_name="Text Colour")


class Statement(Orderable, RichText):
    '''
    Statement on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="statements")
    title = models.CharField(max_length=200, null=True, blank=True)
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Statement.image", "statement"),
        format="Image", max_length=255, null=True, blank=True)
    image_align = models.CharField(max_length=5,
                                   choices=( ('left', 'Left'),('right', 'Right') ),
                                   default='left')        
