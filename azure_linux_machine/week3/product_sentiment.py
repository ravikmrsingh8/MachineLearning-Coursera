import turicreate as tc

# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/amazon_baby.csv
def product_sentiment():
    products = tc.SFrame('amazon_baby.csv')
    selected_words =  ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']
    
    products['word_count'] = tc.text_analytics.count_words(products['review'])
    for word in selected_words:
        products[word] = products['word_count'].apply(lambda word_count : word_count[word] if word in word_count else 0)
    
    products = products[products['rating'] != 3]
    products['sentiment'] = products['rating'] >= 4

    
    train_data, test_data = products.random_split(.8, seed= 0)
    sentiment_classifier_model = tc.logistic_classifier.create(train_data, target='sentiment', features=selected_words, validation_set=test_data)
    print sentiment_classifier_model.coefficients.print_rows(num_rows=12)

    print sentiment_classifier_model.evaluate(test_data)


if __name__ == '__main__':
    product_sentiment()


