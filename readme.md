# SnowChat

Welcome to SnowChat! This is a simple way to query snowflake using natural langague.



## Installation
```
source venv/bin/activate
pip install -r requirements.txt
```

### Configure
Create the following .env folder in the root directory.
```
SNOWFLAKE_ACCOUNT="njjaqdn-kg65139"
SNOWFLAKE_USER="SNOWCHAT_READONLY"
SNOWFLAKE_PASSWORD=<YOUR PASSWORD>
SNOWFLAKE_WAREHOUSE="SNOWCHAT_XLARGE_16C"
SNOWFLAKE_DATABASE="CLOUDINARY"
SNOWFLAKE_SCHEMA="DIM"

OPENAI_API_KEY=<YOUR KEY>

USE_MOCK_SQL="False"
```

## Usage

Example
```
python SnowChatCLI.py -p "Who are the top 5 customers who increased their mrr since last month.  order by mrr increase."
```

Writing to a markup file
```
python -u snowchatcli.py -p "who are the customers that their mrr changed to 0 and previous month was >0. Don't use UPDATED_ATS, LAST_MRR_DOLLAR. limit to 10 top ones" | tee output.md
```

 Help
 ```
 python SnowChatCLI.py -h      
 ```

