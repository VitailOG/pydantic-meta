from types import UnionType
from typing import get_origin, Union

from pydantic.fields import ModelField
from pydantic.main import ModelMetaclass

from pydantic_meta._validators import validate_intersection_between_config_and_attr_class


class Pick(ModelMetaclass):
    """Metaclass for pydantic models basic on typescript utility `Pick<...>`"""

    def __new__(cls, name, bases, namespaces, **kwargs):
        config = namespaces.get('Config', False)

        if config:
            validate_intersection_between_config_and_attr_class(config, kwargs)

        pick_fields = kwargs.pop("pick_fields", []) or getattr(config, 'pick_fields', [])

        # From attributes class
        dn = kwargs.pop("default_none", None)
        default_none = getattr(config, 'default_none', True) if dn is None else dn

        #  Extend pick_fields from parent classes
        for base in bases:
            if pf := getattr(base, '__pick_fields__', False):
                pick_fields.extend(pf)

        instance = super().__new__(cls, name, bases, namespaces, **kwargs)

        # if no pick_fields is set for the model
        if len(pick_fields) == 0:
            return instance

        # Set pick fields to instance
        setattr(instance, "__pick_fields__", pick_fields)

        for field in instance.__fields__:
            model_field: ModelField = instance.__fields__[field]

            # get name or alias
            name = hasattr(model_field, "alias") and model_field.alias or field

            if name not in pick_fields:
                origin = get_origin(model_field.annotation)

                if origin is None or origin not in (UnionType, Union):
                    setattr(model_field, 'allow_none', True)
                    setattr(model_field, 'required', not default_none)

        return instance
