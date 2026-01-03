from pydantic import BaseModel

#request schema (what client sends)
class StudentCreate(BaseModel):
    name: str
    course: str

#response schema (what API returns)
class StudentResponse(BaseModel):
    name: str
    course: str

    class Config():
        orm_mode = True

#request schema for user
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(..., min_length=6, max_length=50)

#response schema for user:
class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config():
        orm_mode = True
