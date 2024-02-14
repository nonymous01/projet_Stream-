from django.contrib import admin

# Register your models here.
from .models import Media,Video
class Media_admin(admin.ModelAdmin):
    readonly_fields=('id',)
admin.site.register(Media,Media_admin)
admin.site.register(Video, Media_admin)

