from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Rider(Base):
    __tablename__ = "riders"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    usual_stop = Column(String, nullable=False)

    rides = relationship("MatatuRide", back_populates="rider")

class MatatuRide(Base):
    __tablename__ = "matatu_rides"

    id = Column(Integer, primary_key=True)
    rider_id = Column(Integer, ForeignKey("riders.id"), nullable=False)
    route = Column(String, nullable=False)
    fare = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    notes = Column(String)
    driver_vibe = Column(String)
    matatu_nickname = Column(String)

    rider = relationship("Rider", back_populates="rides")