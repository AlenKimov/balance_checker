from pydantic import BaseModel


class AddressData(BaseModel):
    address: str
    private_key: str | None
    mnemonic: str | None
    balance: float | None
