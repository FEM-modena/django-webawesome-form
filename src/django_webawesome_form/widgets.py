from django.forms import widgets


class RadioSelect(widgets.ChoiceWidget):
    template_name = "django/forms/widgets/radio.html"
    orientation = "horizontal"
    option_inherits_attrs = False
    checked_attribute = {}
    use_fieldset = False
    use_buttons = False

    def __init__(self, orientation=None, **kwargs):
        if orientation:
            self.orientation = orientation
        super().__init__(**kwargs)

    def get_context(self, name, value, attrs):
        ctx = super().get_context(
            name,
            value,
            {
                **attrs,
                "use_buttons": self.use_buttons,
                # This "value" is targeted at the wa-radio-group element,
                # and it's different from the Django internal "value" (which is a list).
                "value": str(value) if value else "",
                "orientation": self.orientation,
            },
        )
        return ctx

    def id_for_label(self, id_, index=None):
        """
        Don't include for="field_0" in <label> to improve accessibility when
        using a screen reader, in addition, clicking such a label would toggle
        the first input.
        """
        if index is None:
            return ""
        return super().id_for_label(id_, index)


class RadioButtonSelect(RadioSelect):
    template_name = "django/forms/widgets/radio_group_button.html"
    use_buttons = True


class SwitchInput(widgets.CheckboxInput):
    template_name = "django/forms/widgets/switch.html"


class DateInput(widgets.DateInput):
    input_type = "date"


class DateTimeInput(widgets.DateTimeInput):
    input_type = "datetime-local"


class TimeInput(widgets.TimeInput):
    input_type = "time"
