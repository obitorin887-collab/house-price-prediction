from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import joblib

app = FastAPI(title="House Price Prediction")

# Templates
templates = Jinja2Templates(directory="templates")

# Load trained model
model = joblib.load("house_price_rf.pkl")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction_text": None}
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    bedrooms: float = Form(...),
    bathrooms: float = Form(...),
    sqft_living: float = Form(...),
    sqft_lot: float = Form(...),
    floors: float = Form(...),
    waterfront: int = Form(...),
    view: int = Form(...),
    condition: int = Form(...),
    sqft_above: float = Form(...),
    sqft_basement: float = Form(...),
    yr_built: int = Form(...),
    yr_renovated: int = Form(...),
    year: int = Form(...),
    month: int = Form(...)
):

    data = pd.DataFrame([{
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "sqft_lot": sqft_lot,
        "floors": floors,
        "waterfront": waterfront,
        "view": view,
        "condition": condition,
        "sqft_above": sqft_above,
        "sqft_basement": sqft_basement,
        "yr_built": yr_built,
        "yr_renovated": yr_renovated,
        "year": year,
        "month": month
    }])

    prediction = model.predict(data)[0]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction_text": f"Predicted House Price: ${prediction:,.2f}"
        }
    )