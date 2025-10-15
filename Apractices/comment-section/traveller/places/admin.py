from django.contrib import admin
from places.models import Place, Catogory, Gallery,Login_Users,Posts

class GalleryAdmin(admin.TabularInline):
    list_display = ["place","image"]
    model = Gallery

    
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name","place","catogory"]

    inlines = [GalleryAdmin]
admin.site.register(Place, PlaceAdmin)


admin.site.register(Catogory)

admin.site.register(Login_Users)

admin.site.register(Posts)







