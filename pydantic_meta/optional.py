from typing import Optional

from pydantic.main import ModelMetaclass


class AllOptional(ModelMetaclass):
    """
          Example
              class Test(BaseModel, metaclass=AllOptional):
                  name: str
                  age: int
    """

    def __new__(cls, name, bases, namespaces, **kwargs):
        annotations = namespaces.get('__annotations__', {})  # get annotations

        for base in bases:
            annotations.update(base.__annotations__)  # add annotations parents

        for field in annotations:
            annotations[field] = Optional[annotations[field]]  # set optional

        namespaces['__annotations__'] = annotations
        return super().__new__(cls, name, bases, namespaces, **kwargs)
