'''
Author: Woohyeok Choi (2024.03.30)
This code retrieves file_ids from csv document and creates new tables by each of the file's credentials
'''

import gspread
from google.oauth2.service_account import Credentials

# Define the scope
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

# Add credentials to the account
creds = Credentials.from_service_account_file('', scopes=scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Spreadsheet
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1k7zAQCocwwNXi_C-elDJDiJxxWi3BZs1B8wQdZyBLTg/edit#gid=1824587531")

# Select the first worksheet
worksheet = spreadsheet.get_worksheet(0)

# Get all values from the 'file_id' column (assuming 'file_id' is in column A)
file_ids = worksheet.col_values(1)  # Change the index if 'file_id' is in a different column

# Remove the header if present
if file_ids[0] == 'file_id':
    file_ids = file_ids[1:]

# Print the 'file_id' column values
print(file_ids)

