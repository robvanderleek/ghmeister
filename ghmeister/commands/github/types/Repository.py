from pydantic import BaseModel

from ghmeister.commands.github.types.Owner import Owner


class Repository(BaseModel):
    name: str
    full_name: str
    owner: Owner
