import turicreate as tc

#https://d396qusza40orc.cloudfront.net/phoenixassets/image_train_data.csv
#https://d396qusza40orc.cloudfront.net/phoenixassets/image_test_data.csv

def summary():
    image_data = tc.SFrame("image_train_data.csv")
    print image_data['label'].summary();


if __name__ == "__main__":
    summary()

