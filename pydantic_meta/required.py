from pydantic.fields import ModelField
from pydantic.main import ModelMetaclass

from pydantic_meta._validators import validate_intersection_between_config_and_attr_class


class Required(ModelMetaclass):

    def __new__(cls, name, bases, namespaces, **kwargs):
        config = namespaces.get('Config', False)

        if config:
            validate_intersection_between_config_and_attr_class(config, kwargs)

        required_fields = kwargs.pop("required_fields", []) or getattr(config, 'required_fields', [])

        #  Extend required_fields from parent classes
        if required_fields != "__all__":
            for base in bases:
                if pf := getattr(base, '__required_fields__', False):
                    required_fields.extend(pf)

        instance = super().__new__(cls, name, bases, namespaces, **kwargs)

        # Set required fields to instance
        setattr(instance, "__required_fields__", required_fields)

        for field in instance.__fields__:
            model_field: ModelField = instance.__fields__[field]

            # get name or alias
            name = hasattr(model_field, "alias") and model_field.alias or field

            if required_fields == '__all__' or name in required_fields:
                setattr(model_field, 'allow_none', False)
                setattr(model_field, 'required', True)

        return instance
