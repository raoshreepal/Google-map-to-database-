from django.contrib import admin
from .models import Business

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "website", "maps_url")
    search_fields = ("name", "contact", "website")
    list_filter = ("website",)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('name')
    list_per_page = 20

    def has_add_permission(self, request):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            obj.save() 
        