from database import SessionLocal
from fastapi import FastAPI, HTTPException, status
import models
from pydantic import BaseModel
from typing import List, Optional


app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode=True


db = SessionLocal()


@app.get("/")
def index():
    return {"Message": "Hi there my Friend! Welcome!"}

@app.get("/items", response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()
    return items

@app.get("/item/{item_id}", response_model=Item, status_code=200)
def get_an_item(item_id: int):
    item = db.query(models.Item).get({"id": item_id})
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    new_item = models.Item(
        id=item.id,
        name=item.name,
        description=item.description,
        price=item.price,
        on_offer=item.on_offer,
    )
    db_item = db.query(models.Item).filter(models.Item.name==new_item.name).first()
    if db_item is not None:
        raise HTTPException(status_code=409, detail="Item already exists")

    db.add(new_item)
    db.commit()
    return new_item

@app.put("/item/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
def update_an_item(item_id: int, item: Item):
    item_to_update = db.query(models.Item).filter(models.Item.id==item_id).first()
    if item_to_update is None:
        raise HTTPException(status_code=404, detail="Item does not exist")

    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.description = item.description
    item_to_update.on_offer = item.on_offer
    db.commit()
    return item_to_update

@app.delete("/item/{item_id}")
def delete_item(item_id: int):
    item = db.query(models.Item).get({"id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item does not exist")
    db.delete(item)
    db.commit()
    return item

@app.get("/greet")
def greet_optional_message(message:Optional[str]=""):
    return {"message": f"Hi, user. {message}"}
