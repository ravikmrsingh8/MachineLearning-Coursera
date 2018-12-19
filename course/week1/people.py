import pandas as pd


def transform_country(country):
    return "United States" if country == "USA" else country


if __name__ == "__main__":
    # read csv file and returns DataFrame Object
    peoples = pd.read_csv('course/week1/people-example.csv')
    
    # head will return first 5 rows from DataFrame
    print(peoples.head())
    
    # Get Column Values
    print("\n")
    print(peoples['First Name'])
    print(peoples['age'])

    # Adding a new Column
    print("\n")
    peoples["Full Name"] = peoples["First Name"] + " " + peoples["Last Name"]
    print(peoples)

    # Transform country column so that USA is replaced by "United States"
    peoples['Country'] = peoples['Country'].apply(transform_country)

    #Print All data in dataFrame
    print("\n")
    print(peoples)

