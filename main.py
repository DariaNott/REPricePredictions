from contextlib import asynccontextmanager
import joblib
from fastapi import FastAPI
from schemas import HouseFeatures, PredictionResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = joblib.load("models/model_pipeline.joblib")
    yield
    # clear resources here if needed


app = FastAPI(
    lifespan=lifespan,
    title="Real Estate Price Prediction API",
    version="1.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to RE Price Prediction API! Go to /docs for UI."}

@app.post("/predict")
def predict_price(request: HouseFeatures) -> PredictionResponse:
    input_data = [[
        request.SqFtTotLiving,
        request.SqFtLot,
        request.Bedrooms,
        request.Bathrooms,
        request.BldgGrade,
        request.YrBuilt,
        request.NewConstruction,
        request.TrafficNoise,
    ]]

    model = app.state.model
    predicted_price = model.predict(input_data)[0]

    return PredictionResponse(predicted_price_usd=round(predicted_price, 2))
