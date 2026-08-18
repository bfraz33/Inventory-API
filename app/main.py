from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

app = FastAPI(
    title="Inventory & Warehouse API",
    description="Backend API for managing products, warehouses, and inventory.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Inventory API is running"
    }


@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {
            "database": result.scalar()
        }