from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine
from pydantic import BaseModel
from app.database import engine, Base, SessionLocal
from app.models import Item

app = FastAPI(
    title="Inventory & Warehouse API",
    description="Backend API for managing products, warehouses, and inventory.",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

# Class item creation for validation
class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    quantity: int

# App root endpoint
@app.get("/")
def root():
    return {
        "message": "Inventory API is running"
    }

# Testing database connection
@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "database": result.scalar()
        }


# Adding items to the database
@app.post("/items")
def create_item(item: ItemCreate):
    db = SessionLocal()

    new_item = Item(
        name=item.name,
        description=item.description,
        quantity=item.quantity
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    db.close()

    return new_item