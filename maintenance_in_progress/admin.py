from django.contrib import admin

from preferences.admin import PreferencesAdmin

from maintenance_in_progress.models import MaintenanceInProgressPreferences


class MaintenanceInProgressPreferencesAdmin(PreferencesAdmin):
    pass


admin.site.register(
    MaintenanceInProgressPreferences, MaintenanceInProgressPreferencesAdmin
)
