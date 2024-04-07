from pydantic import BaseModel


# Request and response schema.
class Address(BaseModel):
    name: str
    latitude: float
    longitude: float


class ResponseAddress(BaseModel):
    id: int
    name: str
    latitude: float
    longitude: float
