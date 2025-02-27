import openai
import os
import re
import sys

def read_enum_instructions(filename):
    with open(filename, 'r') as file:
        return f"\n\nWhere the {filename.removesuffix(".csv").removeprefix('./lookup/')} is described in this csv:\n{file.read()}\n\n"


def query_chatgpt(question):
    # Initialize the OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)


    # Read the instruciton files of the file
    with open('./instructions.txt', 'r') as file:
        instructions = file.read()


    with open('./schemas/dim.accounts.txt', 'r') as file:
        dim_accounts = file.read()

 
    appendix = ""
    appendix += read_enum_instructions('./lookup/active_component.csv')
    appendix += read_enum_instructions('./lookup/customer_kinds.csv')
    appendix += read_enum_instructions('./lookup/plan_segments.csv')

    # Define the conversation
    messages = [
        {"role": "system", "content": f"{instructions}\n\nBased on the following schema:\n\n{dim_accounts}\n\n{appendix}"},
        {"role": "user", "content": f"{question}"},

    ]

    # Send the message to ChatGPT
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=5000,
        temperature=0.2
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
    



