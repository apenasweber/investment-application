from pydantic import BaseModel


class UserAssetsSchema(BaseModel):
    id: int
    user_id: int
    asset_id: int
    quantidade: int
