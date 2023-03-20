from types import UnionType
from typing import get_origin, Union

from pydantic.main import ModelMetaclass


class Pick(ModelMetaclass):
    """
        Example
            class Test(BaseModel, metaclass=Pick):
                name: str
                age: int

                class Config:
                    pick_fields = ['age']
    """
    def __new__(cls, name, bases, namespaces, **kwargs):
        pick_fields = []
        fields = namespaces.get('__fields__', {})
        config = namespaces.get('Config', False)
        default_none = getattr(config, 'default_none', True)

        if config and (pick_fields := getattr(config, 'pick_fields', False)):
            pick_fields = pick_fields

        for base in bases:
            if base_field := getattr(base.Config, 'pick_fields', False):
                pick_fields.extend(base_field)

            fields.update(base.__fields__)

        instance = super().__new__(cls, name, bases, namespaces, **kwargs)

        for field in instance.__fields__:
            model_field = instance.__fields__[field]
            name = hasattr(model_field, "alias") and model_field.alias or field

            if name not in pick_fields:
                if get_origin(model_field.annotation) not in (UnionType, Union):
                    setattr(model_field, 'allow_none', True)
                    setattr(model_field, 'required', not default_none)

        return instance
