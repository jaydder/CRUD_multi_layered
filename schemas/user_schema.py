from pydantic import BaseModel, StrictStr, StrictInt


class UserSchemas(BaseModel):
    name: StrictStr
    password: StrictInt

    class Config:
        orm_mode = True
