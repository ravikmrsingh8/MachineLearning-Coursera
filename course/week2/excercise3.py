import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math 


# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/home_data.csv

def home_pricing_with_basic_features():
    home_data = pd.read_csv("course/week2/data/home_data.csv")
    features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode']
    X = home_data[features]
    y = home_data['price']
    return evaluateLinearModel(X, y)
    


def home_pricing_with_advanced_features():
    advanced_features = [
        'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode',
        'condition', # condition of house				
        'grade', # measure of quality of construction				
        'waterfront', # waterfront property				
        'view', # type of view				
        'sqft_above', # square feet above ground				
        'sqft_basement', # square feet in basement				
        'yr_built', # the year built				
        'yr_renovated', # the year renovated				
        'lat', 'long', # the lat-long of the parcel				
        'sqft_living15', # average sq.ft. of 15 nearest neighbors 				
        'sqft_lot15', # average lot size of 15 nearest neighbors 
    ]
    home_data = pd.read_csv("course/week2/data/home_data.csv")
    X = home_data[ advanced_features ]
    y = home_data['price']
    return evaluateLinearModel(X, y)


def evaluateLinearModel(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,  random_state=42)
    lm = LinearRegression().fit(X_train,y_train)
    y_predict = lm.predict(X_test)

    root_mean_square_error = math.sqrt(mean_squared_error(y_predict, y_test))
    # root_mean_square_error = getRMSE(y_predict, y_test)
    return root_mean_square_error


def getRMSE(y_predict, y_actual) :
    N = len(y_predict)
    error = 0.0
    y_diff = y_predict-y_actual
    for diff in y_diff:
        error += diff*diff
    
    return math.sqrt(error/N)

if __name__ == "__main__":
    e1 = home_pricing_with_basic_features() 
    e2 = home_pricing_with_advanced_features()
    print( e2, e1)
    print(e1 - e2)


