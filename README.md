from django.forms import CharFieldfrom django.forms import Form

# django-webawesome-form

django-webawesome-form is a Django app that provides a custom form renderer for WebAwesome 
forms. It renders almost all form widgets using the custom components provided by WebAwesome. 
Using this app replaces **every** form rendered in your Django project, including signup,
login, admin, and any third-party apps that use Django forms.

## Beware
This software is still a work in progress. The Django form library covers many cases that 
this library has not yet been tested against. Use it at your own risk.

## Quick start

0. Ensure you're using Django version >= 5.2.

1. Add this Django app and `django.forms` to your `INSTALLED_APPS` setting. **Make sure** to follow this order:
```python
INSTALLED_APPS = [
    ...,
    "django_webawesome_form",
    "django.forms",
]
```

2. Set the Django form renderer setting in your `settings.py` file:
```python
FORM_RENDERER = "django_webawesome_form.renderers.WebAwesomeTemplateSettings"
```

3. Make sure to [include WebAwesome](https://webawesome.com/docs/) in every template where you 
   want to use the form renderer. 

## Widgets
### Radio Select
If you are using the Django form `RadioSelect` widget, use the supplied widget instead.

```python
from django.forms import Form
from django.forms.fields import ChoiceField
# from django.forms.widgets import RadioSelect
from django_webawesome_form.widgets import RadioSelect


class MyForm(Form):
    my_type = ChoiceField(choices=("Type 1", "Type 42", "Type 9"), widget=RadioSelect())
    
```

### Radio Button Select
Use this widget to render radio buttons. It uses `wa-radio` with a button appearance, see 
[Radio Buttons](https://webawesome.com/docs/components/radio-group/#radio-buttons).
```python
from django.forms import Form
from django.forms.fields import ChoiceField
from django_webawesome_form.widgets import RadioButtonSelect


class MyForm(Form):
    my_type = ChoiceField(choices=("Type 1", "Type 42", "Type 9"), widget=RadioButtonSelect())

```

### Switch
Use this widget if you want to render a boolean choice field (better known as _checkbox_) as a 
[switch](https://webawesome.com/docs/components/switch).

```python
from django.forms import Form, CharField, BooleanField
from django_webawesome_form.widgets import SwitchInput


class SearchForm(Form):
    search_text = CharField(label="", required=False)
    include_deleted = BooleanField(widget=SwitchInput())

```

### Use regular, non Custom, HTML Elements
Since this form renderer introduces significant changes in how the HTML elements are rendered, 
you can "opt out" from this behavior by setting the attribute `is_web_component` to `False` on 
the widget class. You can then use regular, not custom, HTML Elements.

```python
from django.forms import Form, CharField
from django.forms.widgets import Widget

class MyWidget(Widget):
   is_web_component = False
   ...

class MyForm(Form):
    my_field = CharField(widget=MyWidget())
```

## Dependencies
This Django app uses a feature of Django 5.2: the `bound_field_class` of the form renderer 
class. See the [Django documentation](https://docs.djangoproject.com/en/5.2/ref/forms/renderers/#django.forms.renderers.BoundField) for more details.

## The label element
WebAwesome custom form elements introduce a significant change to how labels are handled. While in standard 
HTML we always have a `<label for="">` element for the form field (e.g., `<input id="">`), in 
WebAwesome, the label is either an attribute of the element or a slot.

Example:
```html
<!-- Traditional HTML -->
<form>
  <label for="my-form-name">Your Name</label>
  <input id="my-form-name" type="text">
</form>
```

```html
<!-- WebAwesome HTML -->
<form>
  <wa-input id="my-form-name" type="text" label="Your Name"></wa-input>
</form>
```