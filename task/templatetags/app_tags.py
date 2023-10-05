import datetime

from django import template

register = template.Library()


@register.filter(name="get_remain_time")
def get_completed_point(value):
    remain = value.replace(tzinfo=None) - datetime.datetime.now()
    if remain < datetime.timedelta(seconds=1):
        return 0
    return str(remain).split(".")[0]
