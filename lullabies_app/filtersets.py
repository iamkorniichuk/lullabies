from django_filters import rest_framework as filters

from commons.filters import RenamableFilterSetMetaclass
from media.models import MediaSource

from .models import Lullaby


SOURCE_FORMAT_CHOICES = (
    ("audio", "audio"),
    ("video", "video"),
)


def filter_is_empty(queryset, field_name, value):
    if value is None:
        return queryset
    method = "exclude" if value else "filter"
    return getattr(queryset, method)(**{field_name + "__gt": ""})


class LullabyFilterSet(filters.FilterSet, metaclass=RenamableFilterSetMetaclass):
    class Meta:
        model = Lullaby
        fields = "__all__"
        rename = {
            "source_format": "source-format",
        }

    lyrics_is_empty = filters.BooleanFilter(field_name="lyrics", method=filter_is_empty)
    source_format = filters.ChoiceFilter(
        method="filter_source_format", choices=SOURCE_FORMAT_CHOICES
    )

    def filter_source_format(self, queryset, field_name, value):
        if not value:
            return queryset
        sources = MediaSource.objects.filter(format=value).values_list("pk", flat=True)
        return queryset.filter(source__in=sources).all()
