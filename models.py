from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class Plants(Base):
    __tablename__ = 'plants'
    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=False)
    plant_name = Column(String, index=True)
    water_freq = Column(Integer)
    outdoor = Column(Boolean, default=False)
