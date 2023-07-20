from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    cpf = Column(String(11), unique=True, nullable=False)
    nome = Column(String(100), nullable=False)
    saldo_em_conta = Column(Float, default=0)
    senha = Column(String(100), nullable=False)
    codigo_da_conta = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    assets = relationship("UserAssets", back_populates="user")
