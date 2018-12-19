import  turicreate as tc

# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/amazon_baby.csv
def baby_products():
    products = tc.SFrame.read_csv('amazon_baby.csv')
    selected_words = ['awesome', 'great', 'fantastic', 'amazing', 'love', 'horrible', 'bad', 'terrible', 'awful', 'wow', 'hate']
    products['word_count'] = tc.text_analytics.count_words(products['review'])
    for word in selected_words:
        products[word] = products['word_count'].apply(lambda word_count: word_count[word] if word in word_count else 0)
        print word + ':\t ' + str(products[word].sum())
    

if __name__=='__main__':
    baby_products()

