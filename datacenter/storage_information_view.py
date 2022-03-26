from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []

    open_visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in open_visits:
        visit_detail = dict(
            who_entered=visit.passcard.owner_name,
            entered_at=visit.entered_at,
            duration=Visit.format_duration(visit.get_duration()),
            is_strange=visit.is_strange()
        )
        non_closed_visits.append(visit_detail)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
