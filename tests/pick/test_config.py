import pytest

from pydantic_meta.pick import Pick
from pydantic import BaseModel, Field, ValidationError


def test_basic():
    class Test(BaseModel, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = ["name"]

    assert Test(name='Test')


def test_empty_fields():
    class Test(BaseModel, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = []

    with pytest.raises(ValidationError):
        assert Test()


def test_without_pick_fields():
    class Test(BaseModel, metaclass=Pick):
        name: str
        age: int

    assert Test(name='Test', age=23)
    with pytest.raises(ValidationError):
        assert Test(name='Test')


def test_default_not_none():
    class Test(BaseModel, metaclass=Pick):
        name: list[str]
        age: int

        class Config:
            pick_fields = ["name"]
            default_none = False

    assert Test(name=['Test'], age=None)


def test_inheritance_models():

    class Test2(BaseModel, metaclass=Pick):
        first_name: str
        last_name: str

        class Config:
            pick_fields = ["first_name"]

    class Test(Test2):
        name: list[str]
        age: int

        class Config:
            pick_fields = ["name"]

    assert Test(name=['Test'], first_name="Test")


def test_alias_field():

    class Test2(BaseModel, metaclass=Pick):
        schema_: str = Field(..., alias='schema')

        class Config:
            pick_fields = ["schema"]

    class Test(Test2):
        name: list[str]
        age: int

        class Config:
            pick_fields = ["name"]

    assert Test(name=['Test'], schema="Test")
