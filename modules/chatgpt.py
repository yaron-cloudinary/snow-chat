import openai
import os
import re
import sys



def query_chatgpt(question):
    # Initialize the OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)


    # Read the instruciton files of the file
    with open('./instructions.txt', 'r') as file:
        instructions = file.read()


    with open('./schemas/dim.accounts.txt', 'r') as file:
        dim_accounts = file.read()

    with open('./schemas/enum.customer_kinds.csv', 'r') as file:
        enum_customer_kinds = file.read()

    with open('./schemas/lookup.plan_segments.csv', 'r') as file:
        lookup_plan_segments = file.read()

    # Define the conversation
    messages = [
        {"role": "system", "content": f"{instructions}\n\nBased on the following schema:\n\n{dim_accounts}\n\nWhere the customers_kinds are described in this csv:\n{enum_customer_kinds}\n\nAnd plan_segments are descibed here:\n{lookup_plan_segments}"},
        {"role": "user", "content": f"{question}"},

    ]

    # Send the message to ChatGPT
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=500,
        temperature=0.7
    )
    return response










def extract_sql_blocks(text):
    """
    Extracts only the SQL code blocks from the given text and removes everything else.
    """
    pattern = r"```sql(.*?)```"  # Regex pattern to match SQL code blocks
    matches = re.findall(pattern, text, re.DOTALL)  # Find all SQL code blocks
    if matches:
        # Return only the first SQL code block
        return matches[0].strip()
    else:
        return "No SQL code blocks found."
    



