import turicreate as tc

data = tc.SFrame('image_train_data.csv')
test_data = tc.SFrame('image_test_data.csv')


#https://d396qusza40orc.cloudfront.net/phoenixassets/image_train_data.csv
#https://d396qusza40orc.cloudfront.net/phoenixassets/image_test_data.csv

def dog_category():
    dog_data = data[data['label']== 'dog']
    knn_model = tc.nearest_neighbors.create(dog_data, features=['deep_features'],label='id')
    return knn_model



def cat_category():
    cat_data = data[data['label']=='cat']
    knn_model = tc.nearest_neighbors.create(cat_data, features=['deep_features'],label='id')
    return knn_model


def bird_category():
    bird_data = data[data['label']=='bird']
    knn_model = tc.nearest_neighbors.create(bird_data, features=['deep_features'],label='id')
    return knn_model

def automobile_category():
    automobile_data = data[data['label']== 'automobile']
    knn_model = tc.nearest_neighbors.create(automobile_data, features=['deep_features'],label='id')
    return knn_model


if __name__ == "__main__":
    dog_model= dog_category()
    cat_model= cat_category()
    cat = test_data[0:1]
    nearest_cats = cat_model.query(cat)
    nearest_dogs = dog_model.query(cat)
    print nearest_cats
    print nearest_dogs
    print "nearest cats distance mean "
    print nearest_cats['distance'].mean()
    print "nearest dogs distance mean "
    print nearest_dogs['distance'].mean()

    #bird_model= bird_category()
    #auto_model= automobile_category()

