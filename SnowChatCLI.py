import argparse
import os
from dotenv import load_dotenv
from tabulate import tabulate

from modules import chatgpt
from modules import database
from modules import mocksql



load_dotenv()

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Description of your program')

# Add arguments
parser.add_argument('-p', '--prompt', type=str, required=True,  help='You question to Snowflake (required)')
parser.add_argument('-ns', '--nosql', action='store_true', default=False, help='Whether to show the SQL query (default is False)')
# parser.add_argument('-to', '--tableonly', action='store_true', default=False, help='Whether to show only the table (default is False)')

# Parse the arguments
args = parser.parse_args()

print("\n---PROMPT---")
print (args.prompt)

if (os.getenv("USE_MOCK_SQL").lower() == "true"):
    sql = mocksql.get_mock_sql()
else:
    response = chatgpt.query_chatgpt(args.prompt)
    sql = chatgpt.extract_sql_blocks(response.choices[0].message.content)
if (not args.nosql):
    print("\n---SQL---")
    print(sql)
(columns, results) = database.query_snowflake(sql)
print("\n---DATA---")
print(tabulate(results, headers=columns, tablefmt="psql"))  # Use "grid", "pretty", or "psql" format


