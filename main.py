import os
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, HTTPException, Request

import firebase_admin # type: ignore
from firebase_admin import credentials, firestore # type: ignore

import requests
from datetime import datetime


## Initial App
app = FastAPI(
    title="Nestok_Test_Collection",
    description="API for managing Firebase collections, and interacting with FakeStore API.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url = "/openapi.json",
)

## Initial Firestore
cred = credentials.Certificate('firebase_config.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


# Homepage
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
def static_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "app_name": "Nestok Test Collection"})


# Part 1: Basic endpoints
@app.get("/hello")
def hello_world():
    return {"message": "Hello World"}

@app.post("/add")
async def add_timestamp():
    try:
        current_time = datetime.now()
        print(f"\n{current_time}")
        doc_data = {
            "day_of_week": current_time.strftime("%A"),
            "day_of_month": current_time.day,
            "month": current_time.strftime("%b"),
            "timestamp": current_time
        }
        print(f"\n{doc_data}")
        db.collection("sigaram_test_collection").add(doc_data)
        print("Added to Firestore")
        print(f"\nDoc data: {doc_data}")
        return {"message": "Timestamp added successfully", "data": doc_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Part 2: FakeStore API wrapper
FAKE_STORE_API = "https://fakestoreapi.com"

USER_ID = 1 # default userID for API calls
QUANTITY = 1 # default quantity for adding to cart

@app.get("/products")
async def list_products():
    response = requests.get(f"{FAKE_STORE_API}/products")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch products")
    return response.json()

@app.post("/cart/add/{product_id}")
async def add_to_cart(product_id: int):
    product_response = requests.get(f"{FAKE_STORE_API}/products/{product_id}")
    if product_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Product not found")
    
    cart_data = {
        "userId": USER_ID,
        "date": datetime.now().isoformat(),
        "products": [{"productId": product_id, "quantity": QUANTITY}]
    }
    response = requests.post(f"{FAKE_STORE_API}/carts", json=cart_data)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to add to cart")
    
    db.collection("NewsTok_test_collection").add({
        "product_id": product_id,
        "timestamp": firestore.SERVER_TIMESTAMP
    })
    return response.json()

@app.get("/cart")
async def list_cart():
    response = requests.get(f"{FAKE_STORE_API}/carts/{USER_ID}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch cart")
    return response.json()


## RUN!!!
if __name__ == "__main__":
    uvicorn.run(app, port=int(os.environ.get("PORT", 8080)), host="0.0.0.0")