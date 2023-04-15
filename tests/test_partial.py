from pydantic import BaseModel

from pydantic_meta.partial import Partial


def test_base():
    class Test(BaseModel, metaclass=Partial):
        name: str
        age: int

    assert Test(name=None, age=None)

