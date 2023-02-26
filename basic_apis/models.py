from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    city = Column(String)
    state = Column(String)
    pincode = Column(Integer,nullable=False)
    is_active = Column(Boolean, default=True)
    work = relationship("Workhist", back_populates="emp")


class Workhist(Base):
    __tablename__ = "workhist"

    id = Column(Integer, primary_key=True, index=True)
    comp_name = Column(String, index=True, nullable=False)
    from_dt = Column(Date)
    to_dt = Column(Date)
    role = Column(String, nullable=False)
    description = Column(String, index=True)
    emp_id = Column(Integer, ForeignKey("employees.id"))

    emp = relationship("Employee", back_populates="work")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")