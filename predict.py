import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model():
    df = pd.read_csv('data/insurance.csv')
    categorical = ['sex','region','smoker']
    numerical = ['age','bmi','children']
    target = 'charges'

    encoder = OneHotEncoder(sparse_output=False)
    encoded_cat = encoder.fit_transform(df[categorical])
    scaler = StandardScaler()
    scaled_num = scaler.fit_transform(df[numerical])

    X = np.hstack([encoded_cat,scaled_num])
    y = df[target].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.10,random_state=1)
    
    model = LinearRegression()
    model.fit(X_train,y_train)
    score = model.score(X_test, y_test)
    joblib.dump((model,encoder,scaler),'sklearn_price_model.pkl')
    y_pred = model.predict(X_test)
    return score, y_test, y_pred
    
def predict_price(data_dict):
    model, encoder, scaler = joblib.load('sklearn_price_model.pkl')
    cat_features = pd.DataFrame([{
        'sex': data_dict['sex'],
        'region': data_dict['region'],
        'smoker': data_dict['smoker']
    }])
    try:
        num_features = pd.DataFrame([{
            'age': float(data_dict['age']),
            'bmi': float(data_dict['bmi']),
            'children': float(data_dict['children'])
    }])
    except ValueError:
        raise ValueError("Please provide valid numeric values for age, BMI, and children.")
    encoded = encoder.transform(cat_features)
    scaled = scaler.transform(num_features)
    input_data =np.hstack([encoded,scaled])
    prediction = model.predict(input_data)
    return round(float(prediction[0]),2)