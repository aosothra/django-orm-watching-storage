from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    serialized_passcard_visits = []

    for visit in this_passcard_visits:
        serialized_visit = dict(
            entered_at=visit.entered_at,
            duration=visit.get_format_duration(),
            is_strange=visit.is_strange()
        )
        serialized_passcard_visits.append(serialized_visit)

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
