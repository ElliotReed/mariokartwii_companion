from django import template


register = template.Library()


@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds - minutes * 60
    milliseconds = int(round(td.total_seconds() % 1, 3) * 1000)

    return f'{minutes}:{seconds:02}:{milliseconds:03}'
