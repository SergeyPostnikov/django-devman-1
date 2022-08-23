from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_list_or_404


def active_passcards_view(request):
    # Программируем здесь

    all_passcards = get_list_or_404(Passcard, is_active=True)
    context = {
        'active_passcards': all_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
