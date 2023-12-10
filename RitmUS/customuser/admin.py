from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser 

class AdminCustomUser(admin.ModelAdmin):
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_active.short_description = "Activar usuarios"
    make_inactive.short_description = "Desactivar usuarios"
    actions = [make_active, make_inactive]

admin.site.register(CustomUser, AdminCustomUser)