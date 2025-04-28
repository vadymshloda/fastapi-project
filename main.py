from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, ConfigDict


app = FastAPI()

data = {
    "email": "asd@gmail.com",
    "bio": "Some bio",
    "age": "10"
}

data_without_age = {
    "email": "asd@gmail.com",
    "bio": "Some bio",
    #"genger": "male"
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10) 

    model_config = ConfigDict(extra="forbid")


users = []


@app.post("/users")
def add_user(user: UserSchema):
    users.append(user)
    return{"Ok": True, "message": "user added"}


@app.get("/users")
def get_users() -> list[UserSchema]:
    return users


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=130)

#print(repr(UserSchema(**data_without_age)))
#print(repr(UserAgeSchema(**data)))