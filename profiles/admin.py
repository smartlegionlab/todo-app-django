from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'created_at',
    )

    list_filter = ('is_active', 'is_staff', 'created_at')

    list_editable = ('is_active', 'is_staff',)

    search_fields = ('email', 'first_name', 'last_name')

    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'first_name',
                'last_name',
                'is_active',
                'is_staff',
                'telegram_id',
            )
        }),
        ('Additional Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),
        }),
    )

    readonly_fields = ('created_at',)


admin.site.register(Profile, ProfileAdmin)
