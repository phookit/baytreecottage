from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import MapLocal

# never show published or expiry date
#_fieldsets = deepcopy(PageAdmin.fieldsets)
#_fieldsets[0][1]["fields"].remove( ('publish_date', 'expiry_date' ) )


#class MapLocalAdmin(PageAdmin):

#    fieldsets = (
#        deepcopy(_fieldsets[0]),
#            ("details",{
#                'fields': ('content',)
#            }),
#        deepcopy(_fieldsets[1]),
#    )

admin.site.register(MapLocal, PageAdmin)

