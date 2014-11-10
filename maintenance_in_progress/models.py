from django.utils.translation import ugettext_lazy as _, ugettext

dfom preferences.models import Preferences


class MaintenanceInProgressPreferences(Preferences):
    __module__ = "preferences.models"

    in_progress = models.BooleanField(
        default=False,
        help_text=_("Flag that indicates whether maintenance is in progress")
    )
    file_marker = models.CharField(
        max_length=512,
        null=True,
        blank=True,
        help_text=_("Path to a file that indicates maintenance is in progress.")
    )

    class Meta:
        verbose_name_plural = _("Maintenance In Progress Preferences")
