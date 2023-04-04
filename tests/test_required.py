import pytest

from pydantic import BaseModel, ValidationError
from pydantic_meta.required import Required


@pytest.mark.parametrize(
    "args",
    [
        {"name": "Test"},
        {"name": "Test", "age": None}
    ]
)
def test_basic(args):
    class Test(BaseModel, metaclass=Required, required_fields="__all__"):
        name: str
        age: str | int | None = None

    assert Test(name='dsa', age=12)

    with pytest.raises(ValidationError):
        assert Test(**args)


def test_inheritance_models():
    class Test1(BaseModel, metaclass=Required, required_fields=['first_name']):
        first_name: str
        middle_name: str | None = None

    class Test(Test1, required_fields="__all__"):
        name: str

    with pytest.raises(ValidationError):
        assert Test(name='dsa', age=12)
