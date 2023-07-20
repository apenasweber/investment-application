from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class Asset(Base):
    __tablename__ = "asset"
    id = Column(Integer, primary_key=True)
    simbolo = Column(String(10), unique=True, nullable=False)
    preco_atual = Column(Float, nullable=False)
    users = relationship("UserAssets", back_populates="asset")
