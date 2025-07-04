import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score

def train_best_model(X_train, y_train):
    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(random_state=42)
    }

    best_model = None
    best_score = float("inf")

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_train)
        rmse = mean_squared_error(y_train, y_pred, squared=False)

        print(f"{name} RMSE: {rmse:.2f}")
        if rmse < best_score:
            best_model = model
            best_score = rmse

    return best_model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)
    return rmse, r2

def save_model(model, path='models\forecasting_co2_emmision.pkl'):
    """Save model to file."""
    joblib.dump(model, path)
