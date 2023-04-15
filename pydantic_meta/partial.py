from typing import Optional

from pydantic.main import ModelMetaclass


class Partial(ModelMetaclass):
    """Metaclass for pydantic models based on typescript utility `Partial<...>`"""

    def __new__(cls, name, bases, namespaces, **kwargs):
        instance = super().__new__(cls, name, bases, namespaces, **kwargs)

        for field in instance.__fields__:
            model_field = instance.__fields__[field]

            setattr(model_field, 'allow_none', True)
            setattr(model_field, 'required', False)

        return instance
