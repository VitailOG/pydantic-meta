from pydantic import BaseModel

from pydantic_meta.pick import Pick


def test_pick_fields_in_config_default_none_in_attr_class():
    class Test(BaseModel, metaclass=Pick, default_none=False):
        name: str
        age: int

        class Config:
            pick_fields = ["name"]

    assert Test(name='Test', age=None)


def test_two_classes_with_different_pick_fields_settings():
    class Test2(BaseModel, metaclass=Pick, pick_fields=["first_name"]):
        first_name: str
        last_name: str

    class Test(Test2):
        name: list[str]
        age: int

        class Config:
            pick_fields = ["name"]

    assert Test(name=['Test'], first_name="Test")
