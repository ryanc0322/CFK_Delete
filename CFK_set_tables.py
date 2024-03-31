'''
Author: Woohyeok (Ryan) Choi
Date: 2024.03.29
This code sets the new database structure bigQuery for the CFK project
'''
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Set table_id to the ID of the table to create.
project = "carlfilekeeper-database"
dataset = "MM_DD_Export"
table_file = "table_file"
table_relationship = "table_relationship"
table_user = "table_user"

file_table_id = project + "." + dataset + "." + table_file 
relationship_table_id = project + "." + dataset + "." + table_relationship
user_table_id = project + "." + dataset + "." + table_user 

schema_file = [
    bigquery.SchemaField("file_size", "INTEGER"),
    bigquery.SchemaField("file_type", "STRING"),
    bigquery.SchemaField("link_share_status", "INTEGER"),
    bigquery.SchemaField("explicit_shared_status", "INTEGER"), # also counts the last editor
    bigquery.SchemaField("num_shared", "INTEGER"), # number of times file shared
    bigquery.SchemaField("deleted", "INTEGER"), # whether file has been deleted
]

schema_relationship = [
    bigquery.SchemaField("user_email", "STRING"),
    bigquery.SchemaField("file_id", "STRING"),
    bigquery.SchemaField("right", "STRING"), # user's right to the file (view/edit )
    bigquery.SchemaField("marked_for_deletion", "BOOl"),
]

schema_user = [
    bigquery.SchemaField("first_name", "STRING"),
    bigquery.SchemaField("last_name", "STRING"),
    bigquery.SchemaField("user_email", "STRING"),
    bigquery.SchemaField("num_files", "INTEGER"), # number of files that have been explicitly shared to this user
    bigquery.SchemaField("total_size", "INTEGER"), # total size of the files explicitly shared with this user
]

file_table = bigquery.Table(file_table_id, schema=schema_file)
file_table = client.create_table(file_table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(file_table.project, file_table.dataset_id, file_table.table_id)
)

relationship_table = bigquery.Table(relationship_table_id, schema=schema_relationship)
relationship_table = client.create_table(relationship_table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(relationship_table.project, relationship_table.dataset_id, relationship_table.table_id)
)

user_table = bigquery.Table(user_table_id, schema=schema_user)
user_table = client.create_table(user_table)  # Make an API request.
print(
    "Created table {}.{}.{}".format(user_table.project, user_table.dataset_id, user_table.table_id)
)
