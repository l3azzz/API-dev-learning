from django.contrib import admin
from places.models import Place, Catogory, Gallery,Login_Users,Posts,Like,Reply

class GalleryAdmin(admin.TabularInline):
    list_display = ["place","image"]
    model = Gallery

    
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name","place","catogory"]
    inlines = [GalleryAdmin]
admin.site.register(Place, PlaceAdmin)


admin.site.register(Catogory)

admin.site.register(Login_Users)


admin.site.register(Like)


class ReplayAdmin(admin.TabularInline):
    list_display = ["date","username","replay","is_submitted"]
    model = Reply
admin.site.register(Reply)



class PostsAdmin(admin.ModelAdmin):
    inlines = [ReplayAdmin]
admin.site.register(Posts,PostsAdmin)






