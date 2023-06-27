import pytest



# @pytest.mark.parametrize(
#     "data",
#     [
#         (
#             {
#                 "name": "Vitalik",
#                 "first_name": "Zakharkiv",
#                 "last_name": "Volodumyrovych",
#                 "middle_name": "Anton",
#                 "age": 12,
#                 "gender": "male",
#                 "city": "Ternopil",
#                 "street": "Bandera",
#                 "buildings": 12,
#                 "corpus": "a",
#                 "apartment": 1,
#                 "block": "b",
#                 "code": 1234,
#                 "email": "vzakharkiv@gmail.com",
#                 "phone": 3214324324123
#             }
#         ),
#         (
#             {
#                 "name": "Vitalik",
#                 "first_name": None,
#                 "last_name": "Volodumyrovych",
#                 "middle_name": None,
#                 "age": 12,
#                 "gender": None,
#                 "city": "Ternopil",
#                 "street": None,
#                 "buildings": 12,
#                 "corpus": None,
#                 "apartment": 1,
#                 "block": None,
#                 "code": 1234,
#                 "email": "vzakharkiv@gmail.com",
#                 "phone": None
#             }
#         ),
#         (
#             {}
#         ),
#     ],
#     ids=[
#         'classic, full',
#         'classic, none',
#         'classic, empty',
#     ]
# )
# def test_ok222(data, benchmark):
#     from pydantic import BaseModel
#
#     @benchmark
#     def create_model():
#         class Person(BaseModel):
#             name: str | None = None
#             first_name: str | None = None
#             last_name: str | None = None
#             middle_name: str | None = None
#             age: int | None = None
#             gender: str | None = None
#
#             city: str | None = None
#             street: str | None = None
#             buildings: str | None = None
#             corpus: str | None = None
#             apartment: str | None = None
#             block: str | None = None
#
#             code: str | None = None
#             email: str | None = None
#             phone: str | None = None
#         Person(**data)
#
#
# @pytest.mark.parametrize(
#     "data",
#     [
#         (
#             {
#                 "name": "Vitalik",
#                 "first_name": "Zakharkiv",
#                 "last_name": "Volodumyrovych",
#                 "middle_name": "Anton",
#                 "age": 12,
#                 "gender": "male",
#                 "city": "Ternopil",
#                 "street": "Bandera",
#                 "buildings": 12,
#                 "corpus": "a",
#                 "apartment": 1,
#                 "block": "b",
#                 "code": 1234,
#                 "email": "vzakharkiv@gmail.com",
#                 "phone": 3214324324123
#             }
#         ),
#         (
#             {
#                 "name": "Vitalik",
#                 "first_name": None,
#                 "last_name": "Volodumyrovych",
#                 "middle_name": None,
#                 "age": 12,
#                 "gender": None,
#                 "city": "Ternopil",
#                 "street": None,
#                 "buildings": 12,
#                 "corpus": None,
#                 "apartment": 1,
#                 "block": None,
#                 "code": 1234,
#                 "email": "vzakharkiv@gmail.com",
#                 "phone": None
#             }
#         ),
#         (
#             {}
#         ),
#     ],
#     ids=[
#         'with partial, full',
#         'with partial, none',
#         'with partial, empty',
#     ]
# )
# def test_ok1(data, benchmark):
#     from pydantic_meta.partial import Partial
#     from pydantic import BaseModel
#
#     @benchmark
#     def create_model():
#         class Person(BaseModel, metaclass=Partial):
#             name: str
#             first_name: str
#             last_name: str
#             middle_name: str
#             age: int
#             gender: str
#
#             city: str
#             street: str
#             buildings: str
#             corpus: str
#             apartment: str
#             block: str
#
#             code: str
#             email: str
#             phone: str
#
#         Person(**data)
