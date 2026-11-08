from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import models
import schemas
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

@app.get("/plants/", response_model=list[schemas.Plant])
async def get_all_plants(db:db_dependency):
   result = db.query(models.Plants).all()
   if not result:
      raise HTTPException(status_code=404, detail="No plants found")
   return result

@app.get("/plants/{plant_id}", response_model=schemas.Plant)
async def get_plant(plant_id: int, db:db_dependency):
   result = db.query(models.Plants).filter(models.Plants.id == plant_id).first()
   if not result:
      raise HTTPException(status_code=404, detail="Plant not found")
   return result

@app.post("/plants/", response_model=str)
async def add_plant(data: schemas.PlantCreate, db:db_dependency):
   plant_instance = models.Plants(**data.model_dump())
   db.add(plant_instance)
   db.commit()
   db.refresh(plant_instance)
   return "Plant Added"

@app.delete("/plants/{plant_id}", response_model=str)
async def delete_plant(plant_id: int, db:db_dependency):
   to_delete = db.query(models.Plants).filter(models.Plants.id == plant_id).first()
   if not to_delete:
      raise HTTPException(status_code=404, detail="Plant not found")
   db.delete(to_delete)
   db.commit()
   return "Plant Deleted"


