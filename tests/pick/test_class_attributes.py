import pytest

from pydantic import BaseModel, Extra, ValidationError, Field

from pydantic_meta.pick import Pick


def test_basic():
    class Test(BaseModel, metaclass=Pick, pick_fields=["name"]):
        name: str
        age: int

    assert Test(name='Test')


def test_default_not_none():
    class Test(BaseModel, metaclass=Pick, pick_fields=["name"], default_none=False):
        name: list[str]
        age: int

    assert Test(name=['Test'], age=None)

    with pytest.raises(ValidationError):
        assert Test(name=['Test'])


def test_inheritance_models():

    class Test2(BaseModel, metaclass=Pick, pick_fields=["first_name"]):
        first_name: str
        last_name: str

    class Test(Test2, pick_fields=["name"]):
        name: list[str]
        age: int

    assert Test(name=['Test'], first_name="Test")


def test_alias_field():

    class Test2(BaseModel, metaclass=Pick, pick_fields=["schema"]):
        schema_: str = Field(..., alias='schema')

    class Test(Test2, pick_fields=["name"]):
        name: list[str]
        age: int

    assert Test(name=['Test'], schema="Test")
