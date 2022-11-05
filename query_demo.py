from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('credentials.json')

project_id = 'savvy-courage-367218'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
   SELECT *
   FROM bigquery-public-data.imdb.reviews
   LIMIT 1000 """)

results = query_job.result() # Wait for the job to complete.
print(results.to_dataframe())