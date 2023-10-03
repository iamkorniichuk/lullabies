from django.contrib.admin import display
from django.utils.html import format_html


def tag_factory(name, attr_name, format_html):
    attr = lambda obj: getattr(obj, attr_name)
    tag = lambda self, obj: format_html(attr, obj) if attr(obj) else None
    tag.allow_tags = True
    return display(tag, description=name)


def img_tag_factory(name, attr_name, height=48):
    func = lambda attr, obj: format_html(
        '<img src="{}" alt="{}" height="{}">', attr(obj).url, attr(obj).name, height
    )
    return tag_factory(name, attr_name, func)


def a_tag_factory(name, attr_name):
    func = lambda attr, obj: format_html(
        '<a href="{}" target="_blank">{}</a>', attr(obj), attr(obj)
    )
    return tag_factory(name, attr_name, func)


def a_file_tag_factory(name, attr_name):
    func = lambda attr, obj: format_html(
        '<a href="{}" target="_blank">{}</a>', attr(obj).url, attr(obj).name
    )
    return tag_factory(name, attr_name, func)
