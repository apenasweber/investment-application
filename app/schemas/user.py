from pydantic import BaseModel


class User(BaseModel):
    id: int
    cpf: str
    nome: str
    saldo_em_conta: float
    senha: str
    codigo_da_conta: str
    email: str
