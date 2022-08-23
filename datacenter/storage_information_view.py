from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404
from .helpers import format_duration, get_duration, is_visit_long


def storage_information_view(request):
    # Программируем здесь

    non_closed_visits = []

    for visit in get_list_or_404(Visit, leaved_at__isnull=True):    
        data = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        }
        non_closed_visits.append(data)

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
