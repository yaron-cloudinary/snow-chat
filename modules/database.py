import snowflake.connector
import os





def query_snowflake(sql):
    SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
    SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
    SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
    SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
    SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE")
    SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")

    # Establish connection to Snowflake
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )

    # Create a cursor object
    cursor = conn.cursor()

    try:
        # Execute the SQL query
        cursor.execute(sql)

        # Fetch the results
        results = cursor.fetchall()
        columns = [column[0] for column in cursor.description]

    except snowflake.connector.Error as e:
        print(f"Error executing SQL query: {e}")
        columns = []
        results = []

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
    return (columns, results)

