from pydantic import BaseModel


# A dummy model to test packaging
class Dummy(BaseModel):
    id: int
    name: str
    age: int | None = None
