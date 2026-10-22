# Real Estate Price Prediction API

## Overview
This project is an end-to-end Machine Learning web service that predicts residential property prices based on the King County House Sales dataset. It covers the full machine learning lifecycle, from data preprocessing and model training to automated testing and containerized deployment using FastAPI and Docker.

## Tech Stack
* Python (3.12)
* Scikit-learn (Gradient Boosting Regressor, Pipeline, StandardScaler)
* FastAPI & Pydantic (REST API & data validation)
* Pytest (Automated unit and integration testing)
* Docker (Containerization)

## Project Structure
```
REPricePredictions/
│
├── models/
│   └── model_pipeline.joblib   # Trained ML pipeline
├── tests/
│   └── test_main.py            # API integration tests
├── Dockerfile                  # Container configuration
├── main.py                     # FastAPI application entry point
├── schemas.py                  # Pydantic data validation schemas
├── train_model.py              # ML model training script
├── requirements.txt            # Project dependencies
└── kc_house_data.csv           # Dataset
```

## Getting Started Locally

### 1. Clone the repository and navigate to the project folder
```bash
git clone <your-repository-url>
cd REPricePredictions
```
### 2. Create and activate a virtual environment
```bash
python -m venv .venv
```
On Windows:
```bash
.venv\Scripts\activate
```
On macOS/Linux:
```bash
source .venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the FastAPI server
```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000. Interactive Swagger documentation can be accessed at http://127.0.0.1:8000/docs.

## Running Tests
To execute automated tests with pytest, run:

```bash
python -m pytest
```
## Running with Docker
### 1. Build the Docker image
```bash
docker build -t re-price-api .
```
### 2. Run the Docker container
```bash
docker run -d -p 8000:8000 --name re-price-container re-price-api
```
The containerized service will now be accessible at http://localhost:8000/docs.

## API Usage Example
Send a POST request to /predict with the following JSON body:

```
{
  "SqFtTotLiving": 2200.0,
  "SqFtLot": 7500.0,
  "Bedrooms": 3,
  "Bathrooms": 2.5,
  "BldgGrade": 8,
  "YrBuilt": 1995,
  "NewConstruction": 0,
  "TrafficNoise": 0.0
}
```