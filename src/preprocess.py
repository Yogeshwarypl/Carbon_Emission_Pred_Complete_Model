from sklearn.model_selection import train_test_split

def preprocess_data(df):
    df = df.dropna()

    # ✅ Feature Engineering
    df['GDP_per_capita'] = df['GDP'] / df['Population']
    df['Energy_intensity'] = df['Energy Use'] / df['GDP']

    X = df[['GDP', 'Population', 'Energy Use', 'GDP_per_capita', 'Energy_intensity']]
    y = df['co2_emissions']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test
