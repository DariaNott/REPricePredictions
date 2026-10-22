import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib


df = pd.read_csv("kc_house_data.csv")
# Change True/False to 1/0
df["NewConstruction"] = df["NewConstruction"].astype(int)

features = [
    "SqFtTotLiving",  # Загальна житлова площа
    "SqFtLot",  # Площа ділянки
    "Bedrooms",  # Кількість спалень
    "Bathrooms",  # Кількість ванних
    "BldgGrade",  # Оцінка якості будівництва
    "YrBuilt",  # Рік побудови
    "NewConstruction",  # Новобудова
    "TrafficNoise",  # Рівень шуму від транспорту (якщо це число)
]

df = df.dropna(subset=features + ["SalePrice"])

X = df[features].astype(float)  # Приводимо все до чисел
y = df["SalePrice"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42)),
])

pipeline.fit(X_train, y_train)

preds = pipeline.predict(X_test)

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print(f"Середня похибка (MAE): ${mae:.2f}")
print(f"R2 Score: {r2:.2f}")
joblib.dump(pipeline, "models/model_pipeline.joblib")
print("Модель успішно збережена!")