from pydantic import BaseModel


class Owner(BaseModel):
    login: str
