import openai
import os
import re
import sys

def read_lookup_file_instructions(foldername, filename):
    with open(f'{foldername}/{filename}', 'r') as file:
        return f"\nWhere the {filename.removesuffix(".csv").removeprefix('./lookup/')} is described in this csv:\n{file.read()}\n"


def read_lookup_folder_instructions(foldername):
    appendix = ""
    for filename in os.listdir(foldername):
        if filename.endswith(".csv"):
            appendix += read_lookup_file_instructions(foldername, filename)
    return appendix


def query_chatgpt(question):
    # Initialize the OpenAI client
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)


    # Read the instruciton files of the file
    with open('./instructions.txt', 'r') as file:
        instructions = file.read()


    with open('./schemas/dim.accounts.txt', 'r') as file:
        dim_accounts = file.read()

 
    appendix = read_lookup_folder_instructions('./lookup')

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
    



