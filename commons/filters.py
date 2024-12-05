from django_filters.filterset import FilterSetMetaclass


class RenamableFilterSetMetaclass(FilterSetMetaclass):
    @classmethod
    def get_declared_filters(cls, bases, attrs):
        filters = super().get_declared_filters(bases, attrs)
        renamed_filters = cls.rename_filters(filters, attrs)
        return renamed_filters

    @classmethod
    def rename_filters(cls, filters, attrs):
        options = attrs["Meta"].__dict__
        if "rename" in options.keys():
            rename = options["rename"]
            if rename:
                for old, new in rename.items():
                    filters[new] = filters.pop(old)

        return filters
