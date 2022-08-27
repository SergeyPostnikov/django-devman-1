from django.utils.timezone import localtime
from datetime import timedelta


def get_duration(visit):
    if visit.leaved_at is not None:
        return visit.leaved_at - visit.entered_at
    return localtime() - visit.entered_at


def format_duration(duration):  
    return timedelta(days=duration.days, seconds=duration.seconds)


def is_visit_long(visit):
    return get_duration(visit).total_seconds() > 3600
