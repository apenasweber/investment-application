from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class UserAssets(Base):
    __tablename__ = "user_assets"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    asset_id = Column(Integer, ForeignKey("asset.id"))
    quantidade = Column(Integer, nullable=False)
    user = relationship("User", back_populates="assets")
    asset = relationship("Asset", back_populates="users")
