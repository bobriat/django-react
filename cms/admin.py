from django.contrib import admin
from .models import Page, Component

class ComponentInline(admin.StackedInline):
    model = Component
    extra = 1
    ordering = ('-rank',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public')
    inlines = [ ComponentInline, ]
