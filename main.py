from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


class Plant(BaseModel):
 isActive: bool = False
 name: str = None
 water_freq: int = None
 outdoor: bool = False

@app.get("/plants/")
async def get_all_plants(db:db_dependency):
   result = db.query(models.Plants).all()
   if not result:
      raise HTTPException(status_code=404, detail="No plants found")
   return result

@app.get("/plants/{plant_id}")
async def get_plant(plant_id: int, db:db_dependency):
   result = db.query(models.Plants).filter(models.Plants.id == plant_id).first()
   if not result:
      raise HTTPException(status_code=404, detail="Plant not found")
   return result


@app.post("/plants")
async def add_plant(plant: Plant, db: db_dependency):
    db_plant = models.Plants(is_active=plant.isActive, plant_name=plant.name, water_freq=plant.water_freq, outdoor=plant.outdoor)
    db.add(db_plant)
    db.commit()
    db.refresh(db_plant)

