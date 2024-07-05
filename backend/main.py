from fastapi import FastAPI, HTTPException, Query
from typing import List

# Define FastAPI app
app = FastAPI()

# Sample data (using Python lists instead of a database)
men_shoes = [
    {"name": "pants", "price": 99.99},
    {"name": "Running Shoes", "price": 79.99},
    {"name": "Trail Shoes", "price": 89.99},
]

women_shoes = [
    {"name": "Hiking Boots", "price": 89.99},
    {"name": "Running Shoes", "price": 69.99},
    {"name": "Trail Shoes", "price": 79.99},
]

# Endpoint to search for products
@app.get("/api/search", response_model=List[dict])
def search_products(query: str = Query(None, min_length=1)):
    results = []

    # Search logic (Example: Searching in men's and women's shoes)
    for item in men_shoes + women_shoes:
        if query.lower() in item["name"].lower():
            results.append(item)

    return results