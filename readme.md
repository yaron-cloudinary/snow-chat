# SnowChat

Welcome to SnowChat! This is a simple way to query snowflake using natural langague.



## Installation

TBD
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

 Help
 ```
 python SnowChatCLI.py -h      
 ```

