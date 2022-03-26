from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    open_visits = Visit.objects.filter(leaved_at__isnull=True)
    serialized_open_visits = []

    for visit in open_visits:
        serialized_visit = dict(
            who_entered=visit.passcard.owner_name,
            entered_at=visit.entered_at,
            duration=Visit.format_duration(visit.get_duration()),
            is_strange=visit.is_strange()
        )
        serialized_open_visits.append(serialized_visit)

    context = {
        'non_closed_visits': serialized_open_visits,
    }
    return render(request, 'storage_information.html', context)
