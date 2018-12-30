import turicreate as tc
import turicreate.aggregate as agg


def artist_popularity():
    song_data = tc.SFrame('song_data.gl/')
    print song_data.head()
    songs_data = song_data.groupby(key_column_names='artist', operations = {'total_count': agg.SUM('listen_count')})
    songs_data = songs_data.sort('total_count', ascending = True)
    print songs_data.head()
    
if __name__ == '__main__':
    artist_popularity()
