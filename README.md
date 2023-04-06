# Pydantic-Meta
___

## About
Allow to define models where many similar fields

## Installation

```bash
 pip install pydantic-meta
```


## Example

- Partial
### Traditional define

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str | None
    age: int | None
    
User(name=None, age=None)
```
### With metaclass Partial

```python
from pydantic import BaseModel
from pydantic_meta.partial import Partial

class User(BaseModel, metaclass=Partial):
    name: str
    age: int
    
User(name=None, age=None)
```

- Required
### Traditional define
if you want the fields in the parent model to be mandatory in the traditional announcement, it is not possible.
```python
from pydantic import BaseModel

class Name(BaseModel):
    name: str | None = None
    
class User(Name):
    age: int | None
    
User(name="John", age=12)
```
### With metaclass Required

```python
from pydantic import BaseModel
from pydantic_meta.required import Required

class Name(BaseModel):
    name: str | None = None
    
class User(Name, metaclass=Required):
    age: int | None
    
    class Config:
        required_fields=['name']
    
User(name="John", age=12)
```
or
```python
from pydantic import BaseModel
from pydantic_meta.required import Required

class Name(BaseModel):
    name: str | None = None
    
class User(Name, metaclass=Required, required_fields=['name']):
    age: int | None
    
User(name="John", age=12)
```
- Pick
### Traditional define

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    first_name: str | None = None
    age: int | None = None
    
User(name="John")
```
### With metaclass Pick

```python
from pydantic import BaseModel
from pydantic_meta.pick import Pick

class User(BaseModel, metaclass=Pick):
    name: str
    first_name: str 
    age: int
    
    class Config:
        pick_fields = ['name']
    
User(name="John")
```
or
```python
from pydantic import BaseModel
from pydantic_meta.pick import Pick

class User(BaseModel, metaclass=Pick, pick_fields=['name']):
    name: str
    first_name: str
    age: int
    
User(name="John")
```
by default, the fields are set to None, and you can change this by specifying the default_none=False attribute

```python
from pydantic import BaseModel
from pydantic_meta.pick import Pick

class User(BaseModel, metaclass=Pick, pick_fields=['name'], default=False):
    name: str
    first_name: str
    age: int
    
User(name="John", first_name=None, age=None)
```
