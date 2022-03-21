from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in all_visits:
        visit_detail = dict(
            entered_at = visit.entered_at,
            duration = Visit.format_duration(visit.get_duration()),
            is_strange = visit.is_strange()
        )
        this_passcard_visits.append(visit_detail)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
