import turicreate
import turicreate.aggregate as agg
url = 'https://static.turi.com/datasets/rating_data_example.csv'
sf = turicreate.SFrame.read_csv(url)
user_count = sf.groupby(key_column_names='user_id',operations={'count': agg.COUNT()})
print user_count

user_rating_stats = sf.groupby(key_column_names='user_id',  operations={ 'mean_rating': agg.MEAN('rating'),'std_rating': agg.STD('rating')})
print user_rating_stats
