from src.load_data import load_dataset
from src.preprocess import preprocess_data
from src.model import train_best_model, evaluate_model, save_model

def main():
    data = load_dataset("data/climate_change_download_0.xls")
    if data is None:
        return

    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_best_model(X_train, y_train)

    rmse, r2 = evaluate_model(model, X_test, y_test)
    print(f"Model RMSE: {rmse:.2f}")
    print(f"Model R² Score: {r2:.2f}")

    save_model(model, path="models/forecasting_co2_emmision.pkl")

if __name__ == "__main__":
    main()
