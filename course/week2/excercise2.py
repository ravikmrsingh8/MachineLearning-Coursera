import pandas as pd


# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/home_data.csv
def house_price_filtered():
    home_data = pd.read_csv("course/week2/data/home_data.csv")
    home_data_filtered  = home_data[(home_data['sqft_living']>=2000) & (home_data['sqft_living'] <= 4000)]
    # home_data_filtered = home_data[home_data['sqft_living']>4000]
    a = len(home_data_filtered)
    b = len(home_data)
    print(a, b, a/b)



if __name__ == "__main__":
    house_price_filtered()
   