import turicreate as tc


# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/amazon_baby.csv
def product_sentiment():
    products = tc.SFrame('amazon_baby.csv')

    products = products[products['name'] == 'Baby Trend Diaper Champ']
    products['sentiment'] = products['rating'] >= 4


    products['word_count'] = tc.text_analytics.count_words(products['review'])
    
    train_data, test_data = products.random_split(.8, seed= 0)
    sentiment_model = tc.logistic_classifier.create(train_data, target='sentiment', features=['word_count'], validation_set=test_data)
    print sentiment_model.coefficients


    products['predicted'] = sentiment_model.predict(products , output_type='probability')
    print products.sort('predicted', ascending=False)


if __name__ == '__main__':
    product_sentiment()


