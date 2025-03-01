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
parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Show all info returned from chatgpt (default is False)')


# Parse the arguments
args = parser.parse_args()

print("\n# PROMPT")
print ('```\n',args.prompt, '\n```\n')

if (os.getenv("USE_MOCK_SQL").lower() == "true"):
    sql = mocksql.get_mock_sql()
else:
    (messages, response) = chatgpt.query_chatgpt(args.prompt)
    if (args.verbose):
        print("\n# VERBOSE - CHATGPT SYSTEM MESSAGE")
        print(messages[0]["content"].replace('\n', '<br>'))
        print("\n# VERBOSE - CHATGPT RESPONSE")
        print(response.choices[0].message.content)
    sql = chatgpt.extract_sql_blocks(response.choices[0].message.content)
if (not args.nosql):
    print("\n# SQL")
    print('```sql\n',sql, '\n```\n')

print("\n# DATA")
(columns, results) = database.query_snowflake(sql)
print(tabulate(results, headers=columns, tablefmt="github"))  # Use "grid", "pretty", or "psql" format


