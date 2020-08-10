# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Divider(Component):
    """A Divider component.
Material UI Divider component

Keyword arguments:
- inset (boolean; default False): If true, the Divider will be indented
- style (dict; optional): Override the inline-styles of the root element"""
    @_explicitize_args
    def __init__(self, inset=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['inset', 'style']
        self._type = 'Divider'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['inset', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Divider, self).__init__(**args)
