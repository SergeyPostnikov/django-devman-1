from django.utils.timezone import localtime


def get_duration(visit):
    if visit.leaved_at is not None:
        return visit.leaved_at - visit.entered_at
    return localtime() - visit.entered_at


def format_duration(duration):    
    return duration


def is_visit_long(visit):
    return get_duration(visit).seconds > 3600
