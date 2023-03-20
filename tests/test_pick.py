import pytest

from pydantic_meta.pick import Pick
from pydantic import BaseModel, ValidationError, Field


def test_base():
    class Test(BaseModel, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = ['name']

    assert Test(name='tre', age=1)
    assert Test(name='tre', age=None)
    assert Test(name='tre')
    with pytest.raises(ValidationError):
        assert Test()


def test_default_none_false():
    class Test(BaseModel, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = ['name']
            default_none = False

    assert Test(name='tre', age=1)
    assert Test(name='tre', age=None)
    with pytest.raises(ValidationError):
        assert Test(name='tre')


def test_inherit():
    class Child(BaseModel):
        city: str

    class Test(Child, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = ['name']

    assert Test(name='Vitalik', city=None)
    assert Test(name='Vitalik')


def test_own_model_fields():
    class Child(BaseModel):
        city: str

        class Config:
            pick_fields = ['city']

    class Test(Child, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = ['name']

    assert Test(name='Vitalik', city="Ternopil")
    with pytest.raises(ValidationError):
        assert Test(name='Vitalik')


def test_field_alias():
    class Child(BaseModel):
        city_: str = Field(..., alias='city')

    class Test(Child, metaclass=Pick):
        name: str
        age: int

        class Config:
            pick_fields = ['name']

    assert Test(name='Vitalik', city='Ternopil')
    assert Test(name='Vitalik')
