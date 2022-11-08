from pydantic import BaseModel


class AddressData(BaseModel):
    address: str
    balance: float | None
