import turicreate as tc

# Get Csv from https://d396qusza40orc.cloudfront.net/phoenixassets/people_wiki.csv
def top_words():
    peoples = tc.SFrame("people_wiki.csv")
    peoples['word_count'] = tc.text_analytics.count_words(peoples['text'])
    peoples['tf_idf'] = tc.text_analytics.tf_idf(peoples['word_count'])
   
    elton_john = peoples[peoples['name'] == 'Elton John']
    victoria_beckham = peoples[peoples['name'] == 'Victoria Beckham']
    paul_mccartney = peoples[peoples['name'] == 'Paul McCartney']
    word_count_model = tc.nearest_neighbors.create(peoples, features = ['word_count'], label='name', distance='cosine')
    tf_idf_model = tc.nearest_neighbors.create(peoples, features=['tf_idf'], label='name', distance='cosine')

    print "Elton John "
    print  word_count_model.query(elton_john)
    print  tf_idf_model.query(elton_john)

    print "Victoria Beckham"
    print word_count_model.query(victoria_beckham)
    print tf_idf_model.query(victoria_beckham)

if __name__== "__main__":
    top_words()
