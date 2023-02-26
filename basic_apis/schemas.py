from typing import List, Union

from datetime import date
from pydantic import BaseModel


class WorkhistBase(BaseModel):
    comp_name: str
    from_dt: date
    to_dt: date
    role: str
    description: str


class WorkhistCreate(WorkhistBase):
    pass


class Workhist(WorkhistBase):
    id: int
    emp_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True
    
class EmployeeBase(BaseModel):
    name  : str
    email : str
    city  : str
    state  : str
    pincode : int

class Employee(EmployeeBase):
    id: int
    is_active: bool
    work: List[Workhist] = []

    class Config:
        orm_mode = True

class EmployeeCreate(EmployeeBase):
    pass

class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True