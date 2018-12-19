import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot
import seaborn as sns


# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/home_data.csv
def predict_house_price():
    home = pd.read_csv("course/week2/data/home_data.csv") 
    features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'zipcode'] 
    
    print(home[features].head()) 

    X = home[features]
    y = home['price']
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    y_predict = lm.predict(X_test)
    # error vs sqft house
    plot.scatter(X_test['sqft_living'], y_predict-y_test)

    plot.show()


if __name__ == "__main__":
    predict_house_price()