import django_filters as filters

from .models import Lullaby


def filter_is_empty(queryset, field_name, value):
    if value is None:
        return queryset
    method = "exclude" if value else "filter"
    return getattr(queryset, method)(**{field_name + "__gt": ""})


class LullabyFilterSet(filters.FilterSet):
    class Meta:
        model = Lullaby
        fields = "__all__"

    lyrics_is_empty = filters.BooleanFilter(field_name="lyrics", method=filter_is_empty)
