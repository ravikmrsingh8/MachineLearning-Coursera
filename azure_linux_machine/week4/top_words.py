import turicreate as tc

# get csv from https://d396qusza40orc.cloudfront.net/phoenixassets/people_wiki.csv
def top_words():
    peoples = tc.SFrame("people_wiki.csv")
    peoples['word_count'] = tc.text_analytics.count_words(peoples['text'])
    peoples['tf_idf'] = tc.text_analytics.tf_idf(peoples['word_count'])
   
    elton_john = peoples[peoples['name'] == 'Elton John']
    victoria_beckham = peoples[peoples['name'] == 'Victoria Beckham']
    paul_mccartney = peoples[peoples['name'] == 'Paul McCartney']
    # print elton_john
    # print victoria_beckham
    # print paul_mccartney

    top_words_table = elton_john[['word_count']].stack('word_count', new_column_name=['word', 'count']).sort('count', ascending=False)
    top_tfidf_table = elton_john[['tf_idf']].stack('tf_idf', new_column_name=['word', 'tf_idf']).sort('tf_idf', ascending = False)
    print top_words_table
    print top_tfidf_table

    # Find cosine distances between Elton John, Victoria Beckham, Paul McCartney
    print "Elton John & Victoria Beckham "
    print tc.distances.cosine(elton_john['tf_idf'][0], victoria_beckham['tf_idf'][0])

    print "Elton John and Paul McCartney"
    print tc.distances.cosine(elton_john['tf_idf'][0], paul_mccartney['tf_idf'][0])

if __name__ == "__main__":
    top_words()
