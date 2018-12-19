import  turicreate as tc

# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/home_data.csv
def house_prices():
    houses = tc.SFrame.read_csv('home_data.csv')
    print houses.head()

if __name__ == '__main__':
    house_prices()


