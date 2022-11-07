from google.cloud import bigquery
from google.oauth2 import service_account

def query_ratings(role, person):
   credentials = service_account.Credentials.from_service_account_file('credentials.json')

   project_id = 'savvy-courage-367218'
   client = bigquery.Client(credentials= credentials,project=project_id)


   query_statement = """
   SELECT name.primary_name, coalesce(name.nconst, film.{0}) as {0}, film.tconst, rate.reviewer_rating, rate.movie_id
   FROM `bigquery-public-data.imdb.name_basics` name 
   INNER JOIN `bigquery-public-data.imdb.title_crew` film 
   ON name.nconst = film.{0} 
   LEFT JOIN `bigquery-public-data.imdb.reviews` rate
   ON rate.movie_id = film.tconst
   WHERE name.primary_name LIKE '{1}' AND rate.reviewer_rating IS NOT NULL;
   """.format(role, person)

   query_job = client.query(query_statement)


   results = query_job.result() 
   df = results.to_dataframe()
   avg = df[['reviewer_rating']].sum()[0]/df.shape[0]
   result = f'{role[:-1]} {person} has an average rating of {avg}'
   return result
   
def query_numrating(role, person):
   credentials = service_account.Credentials.from_service_account_file('credentials.json')

   project_id = 'savvy-courage-367218'
   client = bigquery.Client(credentials= credentials,project=project_id)


   query_statement = """
   SELECT COUNT(*) 
   FROM `bigquery-public-data.imdb.name_basics` name 
   INNER JOIN `bigquery-public-data.imdb.title_crew` film 
   ON name.nconst = film.{0} 
   LEFT JOIN `bigquery-public-data.imdb.reviews` rate
   ON rate.movie_id = film.tconst
   WHERE name.primary_name LIKE '{1}' AND rate.reviewer_rating IS NOT NULL;
   """.format(role, person)

   query_job = client.query(query_statement)


   results = query_job.result() 
   df = results.to_dataframe()
   result = 'There were {} ratings'.format(df.iloc[0,0])
   return result

def query_total_reviews(role, person):
   credentials = service_account.Credentials.from_service_account_file('credentials.json')

   project_id = 'savvy-courage-367218'
   client = bigquery.Client(credentials= credentials,project=project_id)


   query_statement = """
   SELECT COUNT(*) 
   FROM `bigquery-public-data.imdb.name_basics` name 
   INNER JOIN `bigquery-public-data.imdb.title_crew` film 
   ON name.nconst = film.{0} 
   LEFT JOIN `bigquery-public-data.imdb.reviews` rate
   ON rate.movie_id = film.tconst
   WHERE name.primary_name LIKE '{1}';
   """.format(role, person)

   query_job = client.query(query_statement)


   results = query_job.result() 
   df = results.to_dataframe()
   result = 'There were {} total reviews'.format(df.iloc[0,0])
   return result


   

