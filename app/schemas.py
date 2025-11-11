from pydantic import BaseModel

class ContactBase(BaseModel):
    name: str
    email: str
    mobile: str = None
    home: str = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
