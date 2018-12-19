import pandas as pd

'''
https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.core.groupby.GroupBy.apply.html
'''

# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/home_data.csv
def house_price():
    home_data = pd.read_csv("course/week2/data/home_data.csv")
    zip_price = home_data[['zipcode', 'price']]
    # group by zipcode and apply func avg on each data frame
    zip_price = zip_price.groupby(['zipcode']).apply(lambda x : x.sum()/len(x))
    return zip_price['price'].max()


    

if __name__ == "__main__":
    print(house_price())