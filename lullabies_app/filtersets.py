from rest_framework.filters import OrderingFilter
import django_filters as filters

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


class UseBoostOrderingFilter(OrderingFilter):
    def get_ordering(self, request, queryset, view):
        ordering = super().get_ordering(request, queryset, view)
        if ordering:
            for i in range(len(ordering)):
                field = ordering[i]
                is_desc = field.startswith("-")
                if is_desc:
                    field = field[1:]

                if field == "views":
                    name = "is_boosted"
                    if is_desc:
                        name = "-" + name

                    ordering = list(ordering)
                    ordering.insert(i, name)

        return ordering


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
