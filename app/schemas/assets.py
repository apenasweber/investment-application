from pydantic import BaseModel


class AssetSchema(BaseModel):
    id: int
    simbolo: str
    preco_atual: float
