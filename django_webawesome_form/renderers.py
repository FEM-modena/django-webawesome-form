from django.forms.boundfield import BoundField
from django.forms.renderers import TemplatesSetting


class WebAwesomeBoundField(BoundField):
    def as_widget(self, widget=None, attrs=None, only_initial=False):
        widget = widget or self.field.widget
        if getattr(widget, "is_web_component", True) is True:
            widget_attrs = {
                **(attrs or {}),
                # "label": self.label,
                "disabled": self.field.disabled,
                "wa_slots": {"hint": self.help_text, "label": self.label},
            }
        else:
            widget_attrs = attrs
        return super().as_widget(
            widget=widget,
            attrs=widget_attrs,
            only_initial=only_initial,
        )


def set_slots(context):
    """If the key "wa_slots" is set in widget attrs, pop it out
    from attrs and put in widget.

    """
    if "widget" in context:
        try:
            slots = context["widget"]["attrs"].pop("wa_slots")
        except KeyError:
            slots = {}
        context["widget"]["slots"] = slots
    return context


class WebAwesomeTemplateSettings(TemplatesSetting):
    bound_field_class = WebAwesomeBoundField

    def render(self, template_name, context, request=None):
        context = set_slots(context)
        return super().render(template_name, context, request)
