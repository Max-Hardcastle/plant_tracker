from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Plant(BaseModel):
 name: str = None
 water_freq: int = None
 feed_freq: int = None
 isActive: bool = False
 outdoor: bool = False



@app.get("/")
def read_root():
 return {"message": "Hello from FastAPI!"}


plants = [  {
    "name": "olive tree",
    "water_freq": 10,
    "feed_freq": 60,
    "isActive": True,
    "outdoor": True
  },
  {
    "name": "Lavender",
    "water_freq": 10,
    "feed_freq": 40,
    "isActive": True,
    "outdoor": True
  },
  ]

@app.get("/plants", response_model= list[Plant])
def get_all_plants() -> list:
    return plants

@app.get("/plants/{item_id}", response_model=Plant)
def get_one_plant(item_id: int) -> Plant:
    if item_id < len(plants):
        return plants[item_id]
    else: raise HTTPException(status_code=404, detail= "Plant not found")

@app.post("/plants")
def add_plant(plant: Plant) -> str:
    plants.append(plant)
    return "Success, plant added"

@app.put("/plants/{item_id}")
def update_plant(item_id: int, updated_plant: Plant) -> str:
    if item_id < len(plants):
        plants[item_id] = updated_plant
        return "Success, plant updated"
    else: raise HTTPException(status_code=404, detail= "Plant not found")


@app.delete("/plants/{item_id}")
def delete_plant(item_id: int) -> str:
    if item_id < len(plants):
        plants.pop(item_id)
        return "Success, plant deleted"
    else: raise HTTPException(status_code=404, detail= "Plant not found")