import pandas as pd 
import matplotlib.pyplot as pyplot
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error 
from sklearn.model_selection import train_test_split


# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/home_data.csv
def house_price():
    home = pd.read_csv("course/week2/data/home_data.csv")
    print(home.head())
    

def predict_house_price():
    home_data = pd.read_csv("course/week2/data/home_data.csv")
    
    X = home_data[['sqft_living']]
    y = home_data['price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # linear model
    lm = LinearRegression()
    lm.fit(X_train, y_train)

    y_predict = lm.predict(X_test)

    print("Intercept {}".format(lm.intercept_))
    print("Coeff {}".format(lm.coef_))
    print(pd.DataFrame(lm.coef_, X.columns, columns=['Coeff']))
    

    
    pyplot.subplot(1,2,1)    
    # test set prices
    pyplot.scatter(X_test['sqft_living'], y_test)
    # predicted prices
    pyplot.scatter(X_test['sqft_living'], y_predict)
    pyplot.xlabel("Sqft")
    pyplot.ylabel("Price")

    pyplot.subplot(1,2,2)
    delta_y = y_predict - y_test
    # plot the distribution plot
    sns.distplot(delta_y, bins=20)
    
    pyplot.tight_layout()
    pyplot.show()


if __name__ == "__main__":
    house_price()
    predict_house_price()

