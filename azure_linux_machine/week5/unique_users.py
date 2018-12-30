import turicreate as tc


url = 'https://d396qusza40orc.cloudfront.net/phoenixassets/song_data.csv'
songs = tc.SFrame.read_csv(url)

def unique_users(artist):
    songs_data =  songs[songs['artist']==artist]
    return len(songs_data['user_id'].unique())

def most_unique_users():
    unique_users =  songs.groupby('artist', operations={'total_count':tc.aggregate.COUNT()})
    print 'Most popular artist'
    print unique_users.sort('total_count', ascending=False).print_rows(5)
    print 'Least Popular Artist'
    print unique_users.sort('total_count').print_rows(5)

if __name__=="__main__":
    print songs.head()
    
    print '\n'
    most_unique_users()
    print '\n'

    print 'Kayne West :' + str(unique_users('Kanye West'))
    print 'Foo Fighters: '+str(unique_users('Foo Fighters'))
    print 'Taylor Swift:' +str(unique_users('Taylor Swift'))
    print 'Lady GaGa:' + str(unique_users('Lady GaGa'))
    
