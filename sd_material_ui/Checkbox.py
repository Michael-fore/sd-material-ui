# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Checkbox(Component):
    """A Checkbox component.
Material UI Checkbox component

Keyword arguments:
- checked (boolean; default False): Checkbox is checked if true
- className (string; optional): CSS class name of the root element
- classes (dict; optional): Mapping from MUI Element name to the intended classname for that Element
- disabled (boolean; default False): Checkbox is disabled if true
- id (string; required): The element's ID
- label (string; optional): The label for the checkbox
- name (string; default ''): The name prop of the checkbox
- style (dict; optional): Override the inline styles of the root element"""
    @_explicitize_args
    def __init__(self, checked=Component.UNDEFINED, className=Component.UNDEFINED, classes=Component.UNDEFINED, disabled=Component.UNDEFINED, fireEvent=Component.UNDEFINED, id=Component.REQUIRED, label=Component.UNDEFINED, name=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['checked', 'className', 'classes', 'disabled', 'id', 'label', 'name', 'style']
        self._type = 'Checkbox'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['checked', 'className', 'classes', 'disabled', 'id', 'label', 'name', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Checkbox, self).__init__(**args)
