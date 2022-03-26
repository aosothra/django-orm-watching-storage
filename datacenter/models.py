from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def is_strange(self, standard_duration=60):
        """Checks wether visit duration is compliant with the standard duration.

        Normal security protocols define standard duration of 60 minutes.
        """

        visit_duration = self.get_duration()
        return visit_duration > standard_duration*60

    def get_duration(self) -> float:
        """Returns time duration of the visit in seconds"""

        time_last = (
            self.leaved_at
            if self.leaved_at else localtime()
        )
        duration = time_last - self.entered_at
        return duration.total_seconds()

    def get_format_duration(self):
        """Converts time duration in seconds to a readable format"""
        
        seconds = self.get_duration()

        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f'{hours}h {minutes}m'

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
