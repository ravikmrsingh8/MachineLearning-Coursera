import turicreate as tc

#https://d396qusza40orc.cloudfront.net/phoenixassets/image_train_data.csv
#https://d396qusza40orc.cloudfront.net/phoenixassets/image_test_data.csv

def read_data():
    train_data =tc.SFrame('image_train_data.csv')
    test_data = tc.SFrame('image_test_data.csv')
    data = dict()
    data['train'] = {'dog': filter_data(train_data, 'dog'), 'cat':filter_data(train_data, 'cat'), 'bird':filter_data(train_data, 'bird'), 'automobile':filter_data(train_data, 'automobile')}
    data['test'] =  {'dog': filter_data(test_data, 'dog'), 'cat': filter_data(test_data, 'cat'), 'bird' : filter_data(test_data, 'bird'), 'automobile':filter_data(test_data, 'automobile')}
    return data


def filter_data(data, label):
    return data[data['label']==label]

def train_models(data):
    dog_model = tc.nearest_neighbors.create(data['train']['dog'], features = ['deep_features'], label='id')
    cat_model = tc.nearest_neighbors.create(data['train']['cat'], features = ['deep_features'], label='id')
    bird_model = tc.nearest_neighbors.create(data['train']['bird'], features = ['deep_features'], label='id')
    automobile_model = tc.nearest_neighbors.create(data['train']['automobile'], features = ['deep_features'], label='id')
    return (dog_model, cat_model, bird_model, automobile_model)

def dog_distance_correct(dist):
    return dist['dog_dog'] < dist['dog_auto'] \
            and dist['dog_dog'] < dist['dog_cat'] \
            and dist['dog_dog'] < dist['dog_bird'] 


if __name__ == "__main__":
    data = read_data()
    (dog_model,cat_model, bird_model, auto_model) = train_models(data)
    print dog_model
    dog_dog = dog_model.query(data['test']['dog'], k = 1)['distance']
    dog_cat = cat_model.query(data['test']['dog'], k = 1)['distance']
    dog_bird = bird_model.query(data['test']['dog'], k = 1)['distance']
    dog_auto = auto_model.query(data['test']['dog'], k = 1)['distance']
    distances = tc.SFrame({'dog_dog':dog_dog, 'dog_cat':dog_cat, 'dog_bird': dog_bird, 'dog_auto':dog_auto})
    print distances.apply(dog_distance_correct).sum()
