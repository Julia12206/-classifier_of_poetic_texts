from django.contrib import admin
from .models import Texts
from .models import TextsModel
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Texts._meta.fields]

    class Meta:
        model = Texts

class ProfileAdmin1(admin.ModelAdmin):
    list_display = [i.name for i in TextsModel._meta.fields]

    class Meta:
        model = TextsModel


admin.site.register(Texts, ProfileAdmin)
admin.site.register(TextsModel, ProfileAdmin1)