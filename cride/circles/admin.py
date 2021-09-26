"""Circles Admin."""

# Django
from django.contrib import admin

# Model
from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle Admin"""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'member_limit',
    )
    search_fields = ('slug_name', 'name')
    list_filter = (
        'is_public',
        'verified',
        'is_limited',
    )
